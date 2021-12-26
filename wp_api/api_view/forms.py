from django import forms

class ViewForm(forms.Form):
    user_name = forms.CharField(max_length=30)
    user_email = forms.EmailField()
    user_password = forms.PasswordInput()