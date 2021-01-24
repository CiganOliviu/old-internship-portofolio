from django import forms

from Careers.models import (
    JobsAppliance,
    AvailableJob,
    InternshipsAppliance,
    AvailableInternship,
)


class ApplianceForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    years_of_experience = forms.IntegerField()
    curriculum_vitae = forms.FileField()
    description_of_skills = forms.CharField(widget=forms.Textarea)
    career = forms.ModelChoiceField(queryset=AvailableJob.objects.all())

    class Meta:
        model = JobsAppliance

        fields = (
            'first_name',
            'last_name',
            'email',
            'years_of_experience',
            'curriculum_vitae',
            'description_of_skills',
            'career',
        )


class InternshipApplianceForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    curriculum_vitae = forms.FileField()
    description_of_skills = forms.CharField(widget=forms.Textarea)
    career = forms.ModelChoiceField(queryset=AvailableInternship.objects.all())

    class Meta:
        model = InternshipsAppliance

        fields = (
            'first_name',
            'last_name',
            'email',
            'curriculum_vitae',
            'description_of_skills',
            'career',
        )
