from django.forms import ModelForm
from .models import Bboard

class BbForm(ModelForm):
    class Meta:
        model = Bboard
        fields = ('title', 'content', 'price', 'rubric')
