from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from django.urls import reverse

class UserViewSetTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            fullname='Liam Hallen',
            email='liam@gmail.com',
            phone_number='0765389732',
            password='@HallenLiam',
            type='farmer',
            national_id='NI79365'
        )
        self.url = reverse('users-list')

    def test_create_user(self):
        data = {
            'fullname': 'Paul Jivaji',
            'email': 'paul@example.com',
            'phone_number': '0784935267',
            'password': 'Jivaji@paul',
            'type': 'farmer',
            'national_id': 'NID65476',
            'cooperative_id': ''
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_user(self):
        update_url = reverse('users-detail', args=[self.user.user_id])
        data = {
            'fullname': 'Paul jivaji',
            'email': 'jivaji@gmail.com',
            'phone_number': '0784935267',
            'password': 'PaulJivaji@',
            'type': 'farmer',
            'national_id': 'NID65476',
            'cooperative_id': ''
        }
        response = self.client.put(update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.fullname, 'Paul jivaji')

    def test_delete_user(self):
        delete_url = reverse('users-detail', args=[self.user.user_id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        


