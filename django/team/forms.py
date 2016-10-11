from django import forms

from models import Player
from team.models import Team

class EnrollForm(forms.ModelForm):
        
    team = forms.ModelChoiceField(queryset=Team.objects.all().order_by('name'), to_field_name='pk')
    class Meta:
        model = Player
        fields = ('team',)
