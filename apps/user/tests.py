from django.test import TestCase
from apps.user.serializers import Serializer
from rest_framework.test import APIClient

class TestUserModel(TestCase):

    def create_user(self):
        url = 'http://localhost:8000/users/post'
        data = {
		            "givenName": "user test",
		            "familyName": "family test",
		            "email": "email2@test.com",
		            "password": "xcvsdf",
		            "photo": "...",
	                "is_active": True
                }
        serializer = Serializer(data=data)
        client = APIClient()
        client.post(url, data, format='json')

        self.assertEquals(serializer.data, 'abc')