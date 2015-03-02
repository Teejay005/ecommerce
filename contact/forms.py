from django import forms


class ContactForm(forms.Form):
    Name = forms.CharField(required=False, max_length=100, help_text='100 characters maximum')
    Email = forms.EmailField(required=True)
    Comment = forms.CharField(required=True, widget=forms.Textarea)
