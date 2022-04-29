from django import forms
from .models import Notes
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime,AdminTimeWidget
      

class NotesModelForm(forms.ModelForm):
    class Meta:
        model = Notes
       
    
#fields = "_all_"
        fields = ['title','text','date','time']
       
       
            
        
        
        
