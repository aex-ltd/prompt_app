from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# text prompt model 
class TextPrompt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='textprompt_user')
    title = models.CharField(max_length=60, blank=True, null=True)
    context = models.TextField()
    role = models.TextField()
    goal = models.TextField()
    restrictions = models.TextField()
    audience = models.TextField()
    writing_style = models.TextField()
    tone = models.TextField()
    keywords = models.TextField()
    examples = models.TextField()
    response =  models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email 
    
    class Meta:
        ordering = ['-date']


# file prompt model 
class FilePrompt(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='fileprompt_user')
    file = models.FileField(upload_to='files/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email 
    
    class Meta:
        ordering = ['-date']

    
    
