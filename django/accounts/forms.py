from django import forms

from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from models import UserProfile
from django.utils.translation import ugettext as _

class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['password'].label = _('Password')
        self.fields['password_confirm'].label = _('Password confirm')
        self.fields['first_name'].label = _('First Name')
        self.fields['last_name'].label = _('Last Name')
        self.fields['username'].label = _('User Name')
        self.fields['email'].label = _('email')

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
    
    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['birth_year'].label = _('birth_year')
        
    birth_year = forms.IntegerField(required=True,widget=forms.NumberInput(
                    attrs={'class':'form-control',
                           'placeholder' :'1988',
                    }))
    #You must accept the terms and conditions
    terms = forms.BooleanField(required=True,
                               error_messages={'required': _('terms_mut_be_accepted')},
                label=_('i_accept_terms_conditions')
    )
    captcha = CaptchaField()
    
    class Meta:
        model = UserProfile
        fields = ('birth_year',)
        
    def clean_birth_year(self):
        birth_year = self.cleaned_data.get('birth_year','')
        
        if not isinstance(birth_year, int):
            raise forms.ValidationError(_('birth_year_must_be_integer')) 
        
        if( birth_year < 1920):
            raise forms.ValidationError(_('birth_year_must_gt_1920'))
    
        return birth_year