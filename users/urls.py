from django.urls import path
from .views import UserListAPIView,UserModelViewSet

app_name='users'

urlpatterns = [
    path('',UserListAPIView.as_view())
]