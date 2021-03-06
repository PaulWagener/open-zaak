from django.test import override_settings, tag

from openzaak.components.besluiten.tests.utils import serialise_eio
from openzaak.components.documenten.tests.factories import (
    EnkelvoudigInformatieObjectFactory,
)
from openzaak.utils.query import QueryBlocked
from openzaak.utils.tests import APICMISTestCase

from ...models import ZaakInformatieObject
from ..factories import ZaakInformatieObjectFactory


@tag("cmis")
@override_settings(CMIS_ENABLED=True)
class BlockChangeCMISTestCase(APICMISTestCase):
    def setUp(self) -> None:
        super().setUp()
        eio = EnkelvoudigInformatieObjectFactory.create()
        eio_url = eio.get_url()
        self.adapter.get(eio_url, json=serialise_eio(eio, eio_url))
        self.zio = ZaakInformatieObjectFactory.create(informatieobject=eio_url)

    def test_update(self):
        self.assertRaises(
            QueryBlocked, ZaakInformatieObject.objects.update, titel="new"
        )
        self.assertTrue(self.adapter.request_history)

    def test_delete(self):
        self.assertRaises(QueryBlocked, ZaakInformatieObject.objects.all().delete)
        self.assertTrue(self.adapter.request_history)

    def test_bulk_update(self):
        self.zio.title = "new"
        self.assertRaises(
            QueryBlocked,
            ZaakInformatieObject.objects.bulk_update,
            [self.zio],
            fields=["titel"],
        )
        self.assertTrue(self.adapter.request_history)

    def test_bulk_create(self):
        zio = ZaakInformatieObjectFactory.build()
        self.assertRaises(QueryBlocked, ZaakInformatieObject.objects.bulk_create, [zio])
        self.assertTrue(self.adapter.request_history)
