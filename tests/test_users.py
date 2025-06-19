from django.urls import reverse
from rest_framework.response import Response
from rest_framework.test import APITestCase


class TestSignUp(APITestCase):

    def test_new_sign_up_success(self):
        url = reverse('users:sign-up')
        data = {
            'email': 'test@email.com',
            'password': 'pass1234',
            'first_name': 'John',
            'last_name': 'Rambo',
            'birthday': '1980-07-01',
        }
        response: Response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data,
            {
                'user': {'email': data['email']},
                'profile': {
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'birthday': data['birthday'],
                },
            }
        )
