from django import forms
from django.core.exceptions import ValidationError

from frontpage.models import Contact


class ContactForm(forms.ModelForm):

    confirm_email = forms.EmailField(label="Confirm email", required=True)

    class Meta:
        model = Contact

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email

        return super(ContactForm, self).__init__(*args, **kwargs)