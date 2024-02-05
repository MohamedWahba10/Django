from django import forms
from .models import *
from django.core.exceptions import ValidationError
class MYform(forms.Form):

    id=forms.IntegerField(required=True)
    title=forms.CharField(max_length=255,required=True)
    price=forms.IntegerField(required=True)
    category=forms.CharField(max_length=255,required=True)
    image = forms.ImageField(required=False)
 
 
def clean_id(self):
    user_id=self.cleaned_data['id']
    obj=Product.objects.get(id=user_id).exsists()
    
    if(obj):
        raise ValidationError("must be unique")
    else:
        return True