from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# text prompt model 
class TextPrompt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='textprompt_user')
    title = models.CharField(max_length=300, blank=False, null=False)
    context = models.TextField(max_length=2000, null=True, blank=True)
    role = models.TextField(max_length=2000, null=True, blank=True)
    goal = models.TextField(max_length=2000, null=True, blank=True)
    restrictions = models.TextField(max_length=2000, null=True, blank=True)
    audience = models.TextField(max_length=2000, null=True, blank=True)
    format_result = models.TextField(max_length=2000, null=True, blank=True)
    writing_style = models.TextField(max_length=2000, null=True, blank=True)
    tone = models.TextField(max_length=2000, null=True, blank=True)
    keywords = models.TextField(max_length=2000, null=True, blank=True)
    examples = models.TextField(max_length=2000, null=True, blank=True)
    question =  models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email 
    
    class Meta:
        ordering = ['-date']
 
# hint class 
class Hint(models.Model):
    context = models.TextField(max_length=1000, null=True, blank=True)
    role = models.TextField(max_length=1000, null=True, blank=True)
    goal = models.TextField(max_length=1000, null=True, blank=True)
    restrictions = models.TextField(max_length=1000, null=True, blank=True)
    audience = models.TextField(max_length=1000, null=True, blank=True)
    format_result = models.TextField(max_length=1000, null=True, blank=True)
    writing_style = models.TextField(max_length=1000, null=True, blank=True)
    tone = models.TextField(max_length=1000, null=True, blank=True)
    keywords = models.TextField(max_length=1000, null=True, blank=True)
    examples = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    

