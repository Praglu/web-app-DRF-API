from django import forms
from django.forms import widgets


from .models import ViewModel


class ViewForm(forms.ModelForm):
    class Meta:
        model = ViewModel
        fields = '__all__'
        labels = {
            'user_name': 'Your Name',
            'user_surname': 'Your Surname',
            'age': 'Your Age',
            'email': 'Your e-mail',
            'password': 'Your password'
        }
        widgets = {
            'password' : forms.PasswordInput()
        }

    confirm_password = forms.CharField(widget=widgets.PasswordInput())

    def clean(self):
        cleaned_data = super(ViewForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            self.add_error('confirm_password', 'Passwords does not match!')

        return cleaned_data

