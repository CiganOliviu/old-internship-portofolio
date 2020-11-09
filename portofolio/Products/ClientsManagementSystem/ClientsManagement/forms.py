from django import forms
from ClientsManagement.models import (
    ClientsFeedBack,
    ProjectsRequest,
    MessagesToClient,
)

TYPE_OF_APPS = (
    ("Presentation WebSite", "Presentation WebSite"),
    ("WebApp", "Webapp"),
    ("Mobile App", "Mobile App"),
)


class ClientsFeedBackForm(forms.ModelForm):
    title = forms.CharField(max_length = 200)
    content = forms.CharField(widget = forms.Textarea)

    class Meta:
        model = ClientsFeedBack

        fields = (
            'title',
            'content',
        )


class ProjectsRequestForm(forms.ModelForm):
    project_name = forms.CharField()
    project_description = forms.CharField()
    list_of_functionalities = forms.CharField(widget = forms.Textarea)
    type = forms.ChoiceField(choices = TYPE_OF_APPS)

    class Meta:
        model = ProjectsRequest

        fields = (
            'project_name',
            'project_description',
            'list_of_functionalities',
            'type',
        )