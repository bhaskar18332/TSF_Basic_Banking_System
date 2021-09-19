from .models import *
from django import forms



class data(forms.ModelForm):
	class Meta:
		model = transactions
		fields = ['name1','name2','amount']