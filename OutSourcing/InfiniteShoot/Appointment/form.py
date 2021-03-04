from django import forms
from Appointment.models import Appointment


class DateInput(forms.DateInput):
    input_type = 'date'


class AppointmentForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your first name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your last name'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    phone_number = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Your phone number'}))

    class Meta:
        model = Appointment
        fields = ('first_name', 'last_name', 'email', 'phone_number',
                  'desired_date')

        labels = {
            'desired_date': '',
        }

        widgets = {
            'desired_date': DateInput(),
        }

