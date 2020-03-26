from django.utils.translation import ugettext_lazy as _

from djchoices import ChoiceItem, DjangoChoices


class NLXDirectories(DjangoChoices):
    demo = ChoiceItem("demo", _("Demo"))
    preprod = ChoiceItem("preprod", _("Pre-prod"))
    prod = ChoiceItem("prod", _("Prod"))
