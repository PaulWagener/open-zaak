from relativedeltafield import RelativeDeltaField

from ..forms.fields import RelativeDeltaField as RelativeDeltaFormField


class DurationField(RelativeDeltaField):
    def formfield(self, form_class=None, **kwargs):
        if form_class is None:
            form_class = RelativeDeltaFormField
        return super().formfield(form_class=form_class, **kwargs)
