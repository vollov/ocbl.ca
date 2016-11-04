from django import forms
from django.utils.translation import ugettext as _
from models import Image, Albumn

class UploadFileForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = _('name')
        
    name = forms.CharField(max_length=50, required=True,widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'picture title',
                    }))
    
    albumn = forms.ModelChoiceField(queryset=Albumn.objects.all().order_by('name'), to_field_name='name')
    image = forms.ImageField()
    weight = forms.IntegerField(required=True,widget=forms.NumberInput(
                    attrs={'class':'form-control',
                           'placeholder' :'1',
                    }))
    active = forms.BooleanField(required=False,
                                      initial=False,
                                      label='Publish')
    
    class Meta:
        model = Image
        fields = ('name', 'albumn', 'image', 'weight', 'active')
