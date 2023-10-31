from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='home'),
    path('qestions/<int:id>/', questionView, name='questions'),
    path('file_upload/<int:id>/', file_uploadView, name='file_upload'),
    path('portfolio/', portfolioView, name='portfolio'),
    
    
]