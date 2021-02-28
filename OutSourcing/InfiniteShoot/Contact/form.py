from django import forms
from Contact.models import Newsletter, Contact


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your email'}))

    class Meta:
        model = Newsletter
        fields = ('email', )


class ContactForm(forms.ModelForm):

    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your first name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your last name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your title'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Your message'},
    ), label='')

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'title', 'message')
