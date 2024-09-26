from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .views import dashboard, prompt_view

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('new_prompt/', prompt_view, name='new_prompt'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
