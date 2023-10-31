from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('api.urls')),
    path('ball-user/',include('ball.urls')),
    path('uquv/',include('uquv.urls')),
    path('', edu_login,name='edu_login'),
    path('log_out/', logout_user,name='logout_user'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)