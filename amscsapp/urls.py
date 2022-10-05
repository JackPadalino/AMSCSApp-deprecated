from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
#from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('main.urls')),
    path('users/',include('users.urls')),
    path('classroom/',include('classroom.urls')),
    path('forum/',include('forum.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)