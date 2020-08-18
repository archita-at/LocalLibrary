import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text = "Enter a date between now and 4 weeks (default 3).")
    
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        
        #Check if a date is not in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        
        #Check if a date is in the allowed range (+4 weeks from today).
        if data > datetime.date.today() + datetime.timedelta(weeks = 4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        
        #Remember to always return the cleaned data
        return data
    
class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField(max_length = 100, help_text = 'First Name')
    last_name = forms.CharField(max_length = 100, help_text = 'Last Name')
    email = forms.EmailField(max_length=150, help_text = 'Email')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)