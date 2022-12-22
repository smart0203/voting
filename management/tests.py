from rest_framework.test import APITestCase
from rest_framework import status


class EndpointViewTest(APITestCase):
    def test_basic_auth(self):
        data = {"username": "ccc", "password": "JKJ0203.", "password2": "JKJ0203."}
        response = self.client.post("https://localhost:8000/signup", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        data = {"username": "ccc", "password": "JKJ0203."}
        response = self.client.post("https://localhost:8000/login", data, format='json')
        assert response.status_code == 200

    def get_csrf_token(self):
        response = self.client.get('http://localhost:8000/')
        assert response.status_code == 200
        csrftoken = response.cookies['csrftoken']
        return csrftoken
    
    def restaurant_create(self):
        csrftoken = self.get_csrf_token()
        data = {"name":"Mcdonald"}
        response = self.client.post("https://localhost:8000/restaurant", data, format='json', headers={'X-CSRFToken': csrftoken})
        assert response.status_code == 201
    
    def menu_create(self):
        csrftoken = self.get_csrf_token()
        data = {"restaurant": 1, "items": "Special Menu"}
        response = self.client.post("https://localhost:8000/menu", data, format='json', headers={'X-CSRFToken': csrftoken})
        assert response.status_code == 201
    
    def employee_create(self):
        csrftoken = self.get_csrf_token()
        data = {"name": "Oleksandr"}
        response = self.client.post("https://localhost:8000/employee", data, format='json', headers={'X-CSRFToken': csrftoken})
        assert response.status_code == 201

    def vote_create(self):
        csrftoken = self.get_csrf_token()
        data = {"menu": 1, "employee": 1}
        response = self.client.get("https://localhost:8000/vote", data, format='json', headers={'X-CSRFToken': csrftoken})
        assert response.status_code == 201
    
    def get_currentday_menu(self):
        csrftoken = self.get_csrf_token()
        response = self.client.get("https://localhost:8000/get_currentday_menu", headers={'X-CSRFToken': csrftoken})
        assert response.status_code == 200
    
    def get_currentday_result(self):
        csrftoken = self.get_csrf_token()
        response = self.client.get("https://localhost:8000/get_currentday_result", headers={'X-CSRFToken': csrftoken})
        assert response.status_code == 200