from django.contrib import admin
from django.urls import path, include 
from django.conf import settings 
from django.conf.urls.static import static

from user_prompt.views import dashboard
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_prompt.urls')),
    path('auth/', include('authentication.urls')),
] 
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)