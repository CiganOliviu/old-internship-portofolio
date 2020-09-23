from django import forms
from ClientsManagement.models import (
    FeedBack,
    AskProject,
    DirectClientContact,
)

TYPE_OF_APPS = (
    ("Presentation WebSite", "Presentation WebSite"),
    ("WebApp", "Webapp"),
    ("Mobile App", "Mobile App"),
)

class FeedBackForm(forms.ModelForm):
    title = forms.CharField(max_length = 200)
    content = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = FeedBack

        fields = (
            'title',
            'content',
        )

class AskProjectForm(forms.ModelForm):
    project_name = forms.CharField()
    project_description = forms.CharField()
    list_of_functionalities = forms.CharField(widget = forms.Textarea)
    type = forms.ChoiceField(choices = TYPE_OF_APPS)

    class Meta:
        model = AskProject

        fields = (
            'project_name',
            'project_description',
            'list_of_functionalities',
            'type',
        )

class DirectClientContactForm(forms.ModelForm):
    title = forms.CharField()
    message = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = DirectClientContact

        fields = (
            'title',
            'message',
        )
