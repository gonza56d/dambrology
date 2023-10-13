import datetime

from django import forms


class CustomTextWidget(forms.TextInput):

    def __init__(self):
        super().__init__(attrs={'class': 'form-control mb-3'})


class CustomDateWidget(forms.TextInput):

    def __init__(self):
        super().__init__(attrs={'type': 'date', 'class': 'form-control mb-3'})


class NumerologyForm(forms.Form):

    first_name = forms.CharField(label='Nombres', max_length=300, widget=CustomTextWidget())
    last_name = forms.CharField(label='Apellidos', max_length=300, widget=CustomTextWidget())
    birth = forms.DateField(label='Nacimiento', widget=CustomDateWidget())
