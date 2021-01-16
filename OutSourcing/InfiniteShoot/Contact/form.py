from django import forms
from Contact.models import Newsletter, Contact


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Newsletter
        fields = ('email', )


class ContactForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    title = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'title', 'message')
