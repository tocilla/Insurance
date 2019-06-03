from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import RiskType, RiskField


class TestRiskTypeAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'testuser', email='testuser@test.com', password='testing')
        self.user.save()
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        token.save()

    def test_create_valid_risk_type(self):
        risk_type = {
            'name': 'Name',
            'description': 'Description',
            'risk_fields': [
                {
                    'name': 'Text Field',
                    'type': 'text',
                    'field_options': [],
                    'required': True
                },
                {
                    'name': 'Number Field',
                    'type': 'number',
                    'field_options': [],
                    'required': True
                },
                {
                    'name': 'Checkbox Field',
                    'type': 'boolean',
                    'field_options': [],
                    'required': True
                },
                {
                    'name': 'Select Field',
                    'type': 'option',
                    'field_options': [
                        {
                            'content': 'First'
                        },
                        {
                            'content': 'Second'
                        }
                    ],
                    'required': False
                },
                {
                    'name': 'Date Field',
                    'type': 'date',
                    'field_options': [],
                    'required': False
                }
            ]
        }
        url = reverse('risk_types:risk_type-list')
        response = self.client.post(url, risk_type)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_risk_type_with_blank_name(self):
        risk_type = {
            'name': '',
            'description': 'Description',
            'risk_fields': [
                {
                    'name': 'Text Field',
                    'type': 'text',
                    'field_options': [],
                    'required': True
                }
            ]
        }
        url = reverse('risk_types:risk_type-list')
        response = self.client.post(url, risk_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_type_with_existing_name(self):
        risk_type = {
            'name': "Name",
            'description': 'Description',
            'risk_fields': [
                {
                    'name': 'Text Field With Option',
                    'type': 'text',
                    'field_options': [
                        {
                            'content': 'first',
                            'content': 'second'
                        }
                    ],
                    'required': True
                }
            ]
        }
        RiskType.objects.create(name=risk_type["name"], description=risk_type["description"])
        url = reverse('risk_types:risk_type-list')
        response = self.client.post(url, risk_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_type_without_risk_fields(self):
        risk_type = {
            'name': 'Name',
            'description': 'Description',
            'risk_fields': []
        }
        url = reverse('risk_types:risk_type-list')
        response = self.client.post(url, risk_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_type_with_invalid_type(self):
        risk_type = {
            'name': 'Name',
            'description': 'Description',
            'risk_fields': [
                {
                    'name': 'Invalid Type Field',
                    'type': 'invalid',
                    'field_options': [],
                    'required': True
                }
            ]
        }
        url = reverse('risk_types:risk_type-list')
        response = self.client.post(url, risk_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_type_with_option_field_less_than_two_options(self):
        risk_type = {
            'name': 'Name',
            'description': 'Description',
            'risk_fields': [
                {
                    'name': 'Option Field',
                    'type': 'option',
                    'field_options': [
                        {
                            'content': 'first'
                        }
                    ],
                    'required': True
                }
            ]
        }
        url = reverse('risk_types:risk_type-list')
        response = self.client.post(url, risk_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_type_with_non_option_field_with_options(self):
        risk_type = {
            'name': 'Name',
            'description': 'Description',
            'risk_fields': [
                {
                    'name': 'Text Field With Option',
                    'type': 'text',
                    'field_options': [
                        {
                            'content': 'first',
                            'content': 'second'
                        }
                    ],
                    'required': True
                }
            ]
        }
        url = reverse('risk_types:risk_type-list')
        response = self.client.post(url, risk_type)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_risk_type(self):
        RiskType.objects.create(name='Name 1')
        RiskType.objects.create(name='Name 2')
        url = reverse('risk_types:risk_type-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 2)

    def test_retrieve_risk_type(self):
        risk_type = RiskType.objects.create(name='Name')
        url = reverse('risk_types:risk_type-detail', kwargs={'pk': risk_type.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), risk_type.pk)
