from django import forms

from models import Player
from team.models import Team

class EnrollForm(forms.ModelForm):
        
    team = forms.ModelChoiceField(queryset=Team.objects.all().order_by('name'), to_field_name='pk')
    class Meta:
        model = Player
        fields = ('team',)

class PlayerForm(forms.ModelForm):
        
    number = forms.IntegerField(required=True,widget=forms.TextInput(
                    attrs={'class':'form-control',
                           'placeholder' :'number of the player. e.g. 18',
                    }))
    class Meta:
        model = Player
        fields = ('number',)