from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    author = forms.CharField(max_length=100, required=True)
    publication_date = forms.DateField(widget=forms.SelectDateWidget)
