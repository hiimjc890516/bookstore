from django.urls import path
from main1 import views


app_name = 'main1'
urlpatterns = [
    path('', views.main1, name='main1'),
]