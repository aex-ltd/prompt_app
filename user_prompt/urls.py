from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    dashboard, prompt_context, prompt_audience,
    prompt_examples, prompt_format, prompt_goal, prompt_keywords,prompt_title,
    prompt_restrictions, prompt_role, prompt_tone, prompt_writing_style,
    update_prompt, delete_prompt
)

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('prompt_title/', prompt_title, name='prompt_title'),
    path('prompt_context/', prompt_context, name='prompt_context'),
    path('prompt_audience/', prompt_audience, name='prompt_audience'),
    path('prompt_examples/', prompt_examples, name="prompt_examples"),
    path('prompt_format/', prompt_format, name='prompt_format'),
    path('prompt_goal/', prompt_goal, name='prompt_goal'),
    path('prompt_keywords/', prompt_keywords, name='prompt_keywords'),
    path('prompt_restrictions/', prompt_restrictions, name='prompt_restrictions'),
    path('prompt_role/', prompt_role, name='prompt_role'),
    path('prompt_tone/', prompt_tone, name='prompt_tone'),
    path('prompt_writing_style/', prompt_writing_style, name='prompt_writing_style'),
    path('prompt/<int:pk>/update/', update_prompt, name='update_prompt'),
    path('prompt/<int:pk>/delete/', delete_prompt, name='delete_prompt'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
