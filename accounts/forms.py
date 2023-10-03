from django import forms


class UserRegestrationForm(forms.Form):

    username = forms.CharField()
    email =forms.EmailField()
    password =forms.CharField()
    first=forms.CharField()
    last=forms.CharField()



class UserLoginForm(forms.Form):

    username = forms.CharField()
    password =forms.CharField()

    
    
