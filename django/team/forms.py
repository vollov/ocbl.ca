from django import forms

from models import Player
from team.models import Team

class PlayerForm(forms.ModelForm):

    team = forms.ModelChoiceField(required=True, queryset=Team.objects.all().order_by('name'), 
                    widget=forms.TextInput(
                        attrs={'class':'form-control',
                    }))
    
    class Meta:
        model = Player
        fields = ('team',)
