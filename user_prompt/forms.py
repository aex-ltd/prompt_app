from django import forms 

from .models import TextPrompt, Hint

# text prompt form 
class TextPromptForm(forms.ModelForm):

    class Meta:
        model = TextPrompt
        fields = ['title', 'context', 'role', 'goal', 'restrictions', 'audience','format_result', 'writing_style', 'tone', 'keywords', 'examples']


# prompt title form 
class Title(forms.Form):
    title = forms.CharField(required=True)
    
# prompt context form 
class Context(forms.Form):
    context = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt role form 
class Role(forms.Form):
    role = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt goal form 
class Goal(forms.Form):
    goal = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt restrictions form 
class Restrictions(forms.Form):
    restrictions = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt audience form 
class Audience(forms.Form):
    audience = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt format form 
class FormatResult(forms.Form):
    format_result = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt writing style form 
class WritingStyle(forms.Form):
    writing_style = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt tone form 
class Tone(forms.Form):
    tone = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt keywords form 
class Keywords(forms.Form):
    keywords = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)

# prompt example form 
class Examples(forms.Form):
    example = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}), required=False)


# hint form 
class HintForm(forms.ModelForm):

    class Meta:
        model = Hint
        fields = ['context','role','goal','restrictions','audience','format_result','writing_style','tone','keywords','examples']
