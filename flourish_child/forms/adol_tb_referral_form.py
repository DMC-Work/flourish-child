from django import forms
from django.core.exceptions import ValidationError
from edc_form_validators import FormValidatorMixin

from flourish_form_validations.form_validators import FormValidatorMixin as FlourishFormValidatorMixin
from .child_form_mixin import ChildModelFormMixin

from ..models import TbReferalAdol


class TbReferralAdolForm(ChildModelFormMixin):

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = TbReferalAdol
        fields = '__all__'
