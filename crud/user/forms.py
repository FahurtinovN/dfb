from django import forms

class AddForm(forms.Form):
    name = forms.CharField()
    surname = forms.CharField()
    age = forms.IntegerField()
    birthDay = forms.DateField()
    gender = forms.BooleanField()
