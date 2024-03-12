from datetime import date
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .models import Task

class TaskaAPITest(APITestCase):
    fixtures = ['user', 'task']

    def _authenticate_basic(self):
        self.client.login(username='admin', password='admin') # Basic authentication

    def _authenticate_token(self):
        my_user = User.objects.get(id=1)
        token = Token.objects.create(user=my_user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    # #### #
    # USER #
    # #### #

    def test_get_user(self):
        response = self.client.get('/api/users/')
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 1)
        self.assertIsInstance(response_json, list)
        self.assertIsInstance(response_json[0], dict)

    def test_get_one_user(self):
        response = self.client.get('/api/users/1/')
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 1)
        self.assertEqual(response_json.get('username'), 'admin')
        self.assertEqual(response_json.get('is_staff'), True)        

    def test_post_user(self):        
        url = '/api/users/'
        data = {
            "username": "editor",
            "password": "editor",
        }
        self._authenticate_basic()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_delete_user(self):        
        url = '/api/users/2/'
        self._authenticate_basic()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)

    # #### #
    # TASK #
    # #### #

    def test_get_task(self):
        response = self.client.get('/api/tasks/')
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 1)
        self.assertIsInstance(response_json, list)
        self.assertIsInstance(response_json[0], dict)

    def test_get_one_task(self):
        response = self.client.get('/api/tasks/1/')
        response_json = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response_json), 1)
        self.assertIsInstance(response_json.get('user'), int)
        self.assertIsInstance(response_json.get('task'), int)        
        self.assertIsInstance(response_json.get('start_date'), str)                

    def test_post_task(self):        
        url = '/api/tasks/'
        data = {
            "start_date": "2024-03-11",
            "start_time": "2024-03-11",
            "end_date": "2024-03-12",
            "end_time": "2024-03-11",
            "status": "OP",
            "type": "DA",
            "name": "name",
            "description": "desc",
            "user": 1,
        }
        self._authenticate_basic()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.all().last().user.pk, 1)
        self.assertEqual(Task.objects.all().last().status, 'OP')
        self.assertEqual(Task.objects.all().last().start_date, date(2024, 3, 11))

    def test_put_task(self):        
        url = '/api/tasks/1/'
        data = {
            "id": 1,
            "start_date": "2024-05-11",
            "start_time": "2024-05-11",
            "end_date": "2024-03-12",
            "end_time": "2024-03-11",
            "status": "CL",
            "type": "DA",
            "name": "name",
            "description": "desc",
            "user": 1,
        }
        self._authenticate_basic()
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.all().last().user.pk, 1)
        self.assertEqual(Task.objects.all().last().status, 'CL')
        self.assertEqual(Task.objects.all().last().start_date, date(2024, 5, 11))

    def test_delete_task(self):        
        url = '/api/tasks/1/'
        self._authenticate_basic()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
