from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

from .views import signup_view, login_view, logout_view


urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
] 
urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)