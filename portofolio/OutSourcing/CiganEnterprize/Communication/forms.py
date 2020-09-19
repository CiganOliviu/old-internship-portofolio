from django import forms
from Communication.models import NewsLetter, Contact

class NewsLetterForm(forms.ModelForm):

    email = forms.EmailField()

    class Meta:
        model = NewsLetter
        fields = ('email', )

class ContactForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    title = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'title', 'message', )
