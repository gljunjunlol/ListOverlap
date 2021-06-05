# need to create this forms.py

from django import forms
from django.forms import ModelForm

from .models import *

class StickyStickyForm(forms.ModelForm):

	class Meta:
		model = Sticky
		fields = '__all__'



class StickyStickyForm2(forms.ModelForm):

	class Meta:
		model = Sticky2
		fields = '__all__'
