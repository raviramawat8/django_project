from django import forms


class Signup(forms.Form):
    UserName = forms.Charfield(max_length=100)
    Name = forms.CharField(max_length=100)
    Email = forms.EmailField()
    Password = forms.CharField(max_length=100)
    pass1 = forms.CharField(max_length=100)
    Phoneno = forms.IntegerField(default=0)