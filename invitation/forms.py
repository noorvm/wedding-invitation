from django import forms
from .models import RSVP

class RSVPForm(forms.ModelForm):

    class Meta:
        model = RSVP

        fields = [
            'family_name',
            'guest_count'
        ]