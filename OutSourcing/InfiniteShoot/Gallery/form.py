from django import forms
from Gallery.models import ImagesClient
from .models import BOOLEAN_ANSWER


class ImageClientForm(forms.ModelForm):
    cover_image = forms.ChoiceField(choices=BOOLEAN_ANSWER, initial="NO")
    content_image_one = forms.ChoiceField(choices=BOOLEAN_ANSWER, initial="NO")
    content_image_two = forms.ChoiceField(choices=BOOLEAN_ANSWER, initial="NO")
    content_image_three = forms.ChoiceField(choices=BOOLEAN_ANSWER, initial="NO")
    content_image_four = forms.ChoiceField(choices=BOOLEAN_ANSWER, initial="NO")
    back_image = forms.ChoiceField(choices=BOOLEAN_ANSWER, initial="NO")

    class Meta:
        model = ImagesClient

        fields = (
            'cover_image',
            'content_image_one',
            'content_image_two',
            'content_image_three',
            'content_image_four',
            'back_image',
        )
