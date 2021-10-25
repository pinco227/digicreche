import json

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .api.serializers import SchoolSerializer
from .models import School


class SchoolViewSetTestCase(APITestCase):

    url = reverse('school-list')

    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            user_type=1,
            email='davinci@user.com',
            password='some-very-strong-password')
        self.school = School.objects.create(
            manager=self.user, name='Test Set Up', description="test",
            slug='test-setup', email="davinci@user.com",
            town_or_city='Dublin', county='Dublin', country='IE')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_school_list_authenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_school_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_school_create(self):
        data = {
            "manager": self.user.pk,
            "name": "School DaVinci",
            "description": "automated test school",
            "email": "davinci@school.test",
            "street_address1": "test street 1",
            "street_address2": "test street 2",
            "town_or_city": "Dublin",
            "county": "Dublin",
            "postcode": "d01ab23",
            "country": "IE"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['manager'], self.user.pk)
        self.assertEqual(response.data['slug'], 'school-davinci')
        self.assertEqual(response.data['email'], 'davinci@school.test')

    def test_single_school_retrieve(self):
        serializer_data = SchoolSerializer(instance=self.school).data
        response = self.client.get(reverse('school-detail',
                                           kwargs={'slug': 'test-setup'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(serializer_data, response_data)

    def test_school_update_manager(self):
        data = {
            "manager": self.user.pk,
            "name": 'Test Updated',
            "description": "test updated",
            "slug": 'test-setup',
            "email": "davinci@user.com",
            "town_or_city": 'Dublin',
            "county": 'Dublin',
            "country": 'IE'
        }
        response = self.client.patch(reverse(
            'school-detail', kwargs={'slug': 'test-setup'}), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Updated')
        self.assertEqual(response.data['description'], 'test updated')

    def test_school_update_random_user(self):
        User = get_user_model()
        random_user = User.objects.create_user(email='random@user.com',
                                               password='pasword123123123')
        self.client.force_authenticate(user=random_user)
        data = {'name': 'should not be allowed'}
        response = self.client.put(reverse(
            'school-detail', kwargs={'slug': 'test-setup'}), data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
