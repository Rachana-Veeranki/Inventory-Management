from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemTests(APITestCase):

    def setUp(self):
        self.user = self.client.post('/api/token/', {"username": "test", "password": "test"})
        self.token = self.user.data['access']

    def test_create_item(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        data = {'name': 'Test Item', 'description': 'This is a test item'}
        response = self.client.post(reverse('create_item'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        item = Item.objects.create(name='Test Item', description='This is a test item')
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(reverse('read_item', args=[item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
