from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='homeBall'),
    path('qestions/<int:id>/', questionView, name='questionsBall'),
    path('file_upload/<int:id>/', file_uploadView, name='file_uploadBall'),
    path('repition_ball/<int:id>/', repition_ball, name='repition_ball'),
    path('repition_ball/', portfolioViews, name='portfolioViewBall'),
    
    
]