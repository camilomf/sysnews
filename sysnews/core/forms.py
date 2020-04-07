from django import forms

class TitleSearchForm(forms.Form):
    title = forms.CharField(required=False)