from pyexpat import model
from attr import field
from django.forms import ModelForm,widgets

from .models import project
from django import forms
class ProjectForm(ModelForm):
    class Meta:
        model = project
        fields = ['title','featured_image','description','demo_link','source_link','tags']

        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }
    #basically how to over-write form ke field types !!!! v imppppp
    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        
        self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        self.fields['description'].widget.attrs.update({'class':'input','placeholder':'Add Description'})
        self.fields['demo_link'].widget.attrs.update({'class':'input','placeholder':'Add Demo Link'})
        self.fields['source_link'].widget.attrs.update({'class':'input','placeholder':'Add Source Code Link'})