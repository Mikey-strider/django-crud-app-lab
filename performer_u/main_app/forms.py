from django import forms
from .models import Instructor

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['instructor_name', 'instruction_type', 'instructor_hours']
        widgets = {
            'date_time': forms.DateTimeInput(
                format=('%Y-%m-%d %H:%M'),
                attrs={
                    'placeholder': 'Select a date & time',
                    'type': 'datetime-local'
                }
            )
        }