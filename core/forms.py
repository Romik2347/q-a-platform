from django import forms 
from tinymce.widgets import TinyMCE 
from questions.models import Question
  
class QuestionForm(forms.ModelForm):
    
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 15}))

    class Meta:
        model = Question
        fields = ['content',]