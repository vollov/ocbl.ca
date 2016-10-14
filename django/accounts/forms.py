from django import forms

from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from models import UserProfile
from django.utils.translation import ugettext as _

class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput(
                    attrs={'class':'form-control',
                           'placeholder' :_('Password'),
                    }))
    
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(
                    attrs={'class':'form-control',
                           'placeholder' :_('Password confirm'),
                    }))
    
    first_name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :_('First Name'),
                    }))

    last_name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :_('Last Name'),       
                    }))
    
    username = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :_('User Name'),       
                    }))
    
    email = forms.EmailField(required=True,widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :_('name@gmail.com'),       
                    }))
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')

    def clean_password_confirm(self):
        #cleaned_data = super(UserForm, self).clean()
        # data = self.cleaned_data['recipients']
        password1 = self.cleaned_data.get('password','')
        password2 = self.cleaned_data.get('password_confirm','')
    
        if password1 != password2:
            #msg = "password not match"
            #self.add_error('password_confirm', msg)
            raise forms.ValidationError("Passwords dont match")
    
        return password2
    
class UserProfileForm(forms.ModelForm):
    phone = forms.CharField(required=True,widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'(416)-111-1234',
                    }))
    
    birthday = forms.DateField(required=True,widget=forms.DateInput(
                    attrs={'class':'form-control',
                           'placeholder' :'1978-10-25',
                    }))
    
    height = forms.IntegerField(required=True,widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :_('your hight in cms. e.g. 180'),
                    }))
    
    captcha = CaptchaField()
    
    class Meta:
        model = UserProfile
        fields = ('phone','birthday', 'height')