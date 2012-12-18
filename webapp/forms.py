
from django import forms
from models import *



class myfilterForm(forms.ModelForm):
	
    class Meta:
        model = myfilter	
        # exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(myfilterForm, self).__init__(*args, **kwargs)

