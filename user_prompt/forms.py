from django import forms 

from .models import TextPrompt, Hint

# text prompt form 
class TextPromptForm(forms.ModelForm):

    class Meta:
        model = TextPrompt
        fields = ['title', 'context', 'role', 'goal', 'restrictions', 'audience','format_result', 'writing_style', 'tone', 'keywords', 'examples']

# prompt context form 
class Context(forms.ModelForm):
    context = forms.CharField(required=False)

# prompt role form 
class Role(forms.ModelForm):
    role = forms.CharField(required=False)

# prompt goal form 
class Goal(forms.ModelForm):
    goal = forms.CharField(required=False)

# prompt restrictions form 
class Restrictions(forms.ModelForm):
    restrictions = forms.CharField(required=False)

# prompt audience form 
class Audience(forms.ModelForm):
    audience = forms.CharField(required=False)

# prompt format form 
class FormatResult(forms.ModelForm):
    format_result = forms.CharField(required=False)

# prompt writing style form 
class WritingStyle(forms.ModelForm):
    writing_style = forms.CharField(required=False)

# prompt tone form 
class Tone(forms.ModelForm):
    tone = forms.CharField(required=False)

# prompt keywords form 
class Keywords(forms.ModelForm):
    keywords = forms.CharField(required=False)

# prompt example form 
class Examples(forms.ModelForm):
    example = forms.CharField(required=False)


# hint form 
class HintForm(forms.ModelForm):

    class Meta:
        model = Hint
        fields = ['context','role','goal','restrictions','audience','format_result','writing_style','tone','keywords','examples']
