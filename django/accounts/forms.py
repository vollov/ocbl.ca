from django import forms

from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(required=True, widget=forms.PasswordInput(
                    attrs={'class':'form-control',
                           'placeholder' :'Password',
                    }))
    
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(
                    attrs={'class':'form-control',
                           'placeholder' :'Password confirm',
                    }))
    

    first_name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'First Name',       
                    }))

    last_name = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'Last Name',       
                    }))
    
    username = forms.CharField(required=True, widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'User Name',       
                    }))
    
    email = forms.EmailField(required=True,widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'name@gmail.com',       
                    }))
    
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')

    def clean_password_confirm(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_confirm')
    
        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
    
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
    
    captcha = CaptchaField()
    
    class Meta:
        model = UserProfile
        fields = ('phone','birthday')