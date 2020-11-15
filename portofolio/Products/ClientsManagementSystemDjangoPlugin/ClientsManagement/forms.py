from django import forms
from ClientsManagement.models import (
    ClientsFeedBack,
    ProjectsRequest,
    ClientsDetail,
    TYPE_OF_APPS,
    TYPE_OF_CLIENT,
)


class ClientsFeedBackForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = ClientsFeedBack

        fields = (
            'title',
            'content',
        )


class ProjectsRequestForm(forms.ModelForm):
    project_name = forms.CharField()
    project_description = forms.CharField()
    list_of_functionalities = forms.CharField(widget=forms.Textarea)
    type = forms.ChoiceField(choices=TYPE_OF_APPS)

    class Meta:
        model = ProjectsRequest

        fields = (
            'project_name',
            'project_description',
            'list_of_functionalities',
            'type',
        )


class ClientsDetailForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    client_description = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    phone_number = forms.CharField()
    website = forms.URLField()
    social_media_presence = forms.URLField()
    profile_image = forms.ImageField()
    type_of_client = forms.ChoiceField(choices=TYPE_OF_CLIENT)

    class Meta:
        model = ClientsDetail

        fields = (
            'first_name',
            'last_name',
            'client_description',
            'email',
            'phone_number',
            'website',
            'social_media_presence',
            'profile_image',
            'type_of_client',
        )

