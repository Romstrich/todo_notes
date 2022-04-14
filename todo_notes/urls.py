"""todo_notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authors.views import AuthorModelViewSet, BiographyModelViewSet,BookModelViewSet
from todo.views import ProjectModelViewSet, TodoModelViewSet
from users.views import  UserListAPIView,UserRetrieveAPIView,UserUpdateAPIView #UserModelViewSet,

router=DefaultRouter()
# router.register('authors',AuthorModelViewSet)
#router.register('users',UserModelViewSet)
# router.register('biographyes',BiographyModelViewSet)
# router.register('books',BookModelViewSet)
# router.register('projects',ProjectModelViewSet)
# router.register('todo_notes',TodoModelViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/',include('rest_framework.urls')),
    path('api/',include(router.urls)),

    path('api/user/list/',UserListAPIView.as_view()),
    path('api/user/detail/<int:pk>/',UserRetrieveAPIView.as_view()),
    path('api/user/update/<int:pk>/', UserUpdateAPIView.as_view())


]
