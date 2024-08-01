from django import forms
from .models import Student

gen = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        labels = {
            'sid' : 'Student ID',
            'name' : 'Student Name'
        }

        widgets = {
            'sid' : forms.NumberInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'marks' : forms.NumberInput(attrs={'class':'form-control'}),
            'gender' : forms.RadioSelect(choices=gen),
            'city' : forms.TextInput(attrs={'class':'form-control'})
        }