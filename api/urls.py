from django.urls import path
from .views import TesterAPI


urlpatterns = [
    path('tester', TesterAPI.as_view(), name="tester"),
    
]
