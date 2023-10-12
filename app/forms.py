from django import forms


class NumerologyForm(forms.Form):

    first_name = forms.CharField(max_length=300)
    last_name = forms.CharField(max_length=300)
    birth = forms.DateField()
