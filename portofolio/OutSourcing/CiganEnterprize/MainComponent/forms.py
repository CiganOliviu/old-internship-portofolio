from django import forms
from MainComponent.models import JobsAppliance, AvaibleJob

class ApplianceForm(forms.ModelForm):

    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    years_of_experience = forms.IntegerField()
    curriculum_vitae = forms.FileField()
    description_of_skills = forms.CharField(widget = forms.Textarea)
    carrer = forms.ModelChoiceField(queryset = AvaibleJob.objects.all())

    class Meta:
        model = JobsAppliance

        fields = (
            'first_name',
            'last_name',
            'email',
            'years_of_experience',
            'curriculum_vitae',
            'description_of_skills',
            'carrer',
        )
