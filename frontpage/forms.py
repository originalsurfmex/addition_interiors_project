from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, label='subject',
                              widget=forms.TextInput(attrs={'placeholder': 'I want a free estimate'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6, 'cols': 19, 'placeholder': 'I am in need of flooring...'}))
    sender = forms.EmailField(
        required=False, widget=forms.TextInput(attrs={'placeholder': 'Email (optional)'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Phone Number (optional)'}))


class SMSForm(forms.Form):
    subject = forms.CharField(max_length=100, label='subject',
                              widget=forms.TextInput(attrs={'placeholder': 'I want a free estimate'}))
    message = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6, 'cols': 19, 'placeholder': 'Text Messsage'}))
    sender = forms.EmailField(
        required=False, widget=forms.TextInput(attrs={'placeholder': 'Email (optional)'}))
    cell = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Cell Number (optional)'}))
