from django import forms

from models import Image

class UploadFileForm(forms.Form):
    
    class Meta:
        model = Image
        fields = ('name', 'albumn', 'image', 'weight', 'active')