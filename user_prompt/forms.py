from django import forms 

from .models import TextPrompt, Hint

# text prompt form 
class TextPromptForm(forms.ModelForm):

    class Meta:
        model = TextPrompt
        fields = ['title', 'context', 'role', 'goal', 'restrictions', 'audience','format_result', 'writing_style', 'tone', 'keywords', 'examples']
        
