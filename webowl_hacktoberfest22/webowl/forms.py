from django import forms
from django import forms

class SearchWeb(forms.Form):
    url = forms.CharField(label="URL / IP", max_length=100)