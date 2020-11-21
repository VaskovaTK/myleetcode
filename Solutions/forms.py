from django import forms

class SolForm (forms.Form):
    solution = forms.CharField (label ="solution", widget=forms.Textarea(attrs={'class':'form_control'}))
