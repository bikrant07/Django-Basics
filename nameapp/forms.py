from django import forms 

class NameForm(forms.Form):
    name=forms.CharField(max_length=100, label="Enter your name")
    email=forms.EmailField(label="Enter your email")
