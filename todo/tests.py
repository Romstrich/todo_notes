from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory,force_authenticate,APIClient,APISimpleTestCase,APITestCase
from mixer.backend.django import mixer
#from django.contrib.auth.models import User

from users.models import User
from todo.views import ProjectModelViewSet
from todo.views import TodoModelViewSet

# Create your tests here.


class TestProjectViewSet(TestCase):

    def setUp(self) -> None:
        self.name='admin'
        self.password='admin_01'
        self.email='admin@super.ru'

        self.admin=User.objects.create_user(username=self.name,password=self.password,email=self.email)
        self.data={'name':'new_project','users':[1,2,3]}
        self.data_put={'name':'new_project1','users':[1,2,3]}
        self.url='/api/projects'


    def test_get_list(self):
        factory=APIRequestFactory()

        request=factory.get(self.url)
        view=ProjectModelViewSet.as_view({'get':'list'})
        response=view(request)

        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def tearDown(self) -> None:
        pass

