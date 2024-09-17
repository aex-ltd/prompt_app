from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .views import dashboard, ask_ai_view

urlpatterns = [
    path('user/dashboard/', dashboard, name='dashboard'),
    path('ask_ai/', ask_ai_view, name='ask_ai'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
