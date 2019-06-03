from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Risk, RiskInput
from risk_types.models import RiskType, RiskField


class TestRiskTypeAPIViews(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            'testuser', email='testuser@test.com', password='testing')
        self.user.save()
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        token.save()

        self.risk_type = RiskType.objects.create(name='name', description="description")
        RiskField.objects.create(name='Required Text Field',
                                 risk_type_id=self.risk_type.pk, type='text', required=True)
        RiskField.objects.create(
            name='Text Field', risk_type_id=self.risk_type.pk, type='text', required=False)

    def test_create_valid_risk(self):
        risk = {
            'name': 'Name',
            'risk_type': self.risk_type.pk,
            'risk_inputs': [
                {
                    'risk_field': self.risk_type.risk_fields.all()[0].pk,
                    'value':'required value'
                },
                {
                    'risk_field': self.risk_type.risk_fields.all()[1].pk,
                    'value':'value'
                }
            ]
        }
        url = reverse('risks:risk-list')
        response = self.client.post(url, risk)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_risk_with_blank_name(self):
        risk = {
            'name': '',
            'risk_type': self.risk_type.pk,
            'risk_inputs': [
                {
                    'risk_field': self.risk_type.risk_fields.all()[0].pk,
                    'value':'required value'
                },
                {
                    'risk_field': self.risk_type.risk_fields.all()[1].pk,
                    'value':'value'
                }
            ]
        }
        url = reverse('risks:risk-list')
        response = self.client.post(url, risk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_with_existing_name(self):
        risk = {
            "name": "Name",
            "risk_type": self.risk_type.pk,
            "risk_inputs": [
                {
                    "risk_field": self.risk_type.risk_fields.all()[0].pk,
                    "value":"value"
                },
                {
                    "risk_field": self.risk_type.risk_fields.all()[1].pk,
                    "value":"value"
                }
            ]
        }
        Risk.objects.create(name=risk["name"], risk_type_id=self.risk_type.pk)
        url = reverse('risks:risk-list')
        response = self.client.post(url, risk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_without_risk_inputs(self):
        risk = {
            "name": "Name",
            "risk_type": self.risk_type.pk,
        }
        url = reverse('risks:risk-list')
        response = self.client.post(url, risk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_with_invalid_risk_type_id(self):
        risk = {
            "name": "Name",
            "risk_type": self.risk_type.pk + 999,
            "risk_inputs": [
                {
                    "risk_field": self.risk_type.risk_fields.all()[0].pk,
                    "value":"value"
                }
            ]
        }
        url = reverse('risks:risk-list')
        response = self.client.post(url, risk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_with_invalid_risk_field_id(self):
        risk = {
            "name": "Name",
            "risk_type": self.risk_type.pk,
            "risk_inputs": [
                {
                    "risk_field": self.risk_type.risk_fields.all()[0].pk,
                    "value":"value"
                },
                {
                    "risk_field": self.risk_type.risk_fields.all()[1].pk + 999,
                    "value":"value"
                }
            ]
        }
        url = reverse('risks:risk-list')
        response = self.client.post(url, risk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_risk_with_blank_required_input(self):
        risk = {
            'name': 'Name',
            'risk_type': self.risk_type.pk,
            'risk_inputs': [
                {
                    'risk_field': self.risk_type.risk_fields.all()[0].pk,
                    'value':''
                },
                {
                    'risk_field': self.risk_type.risk_fields.all()[1].pk,
                    'value':'value'
                }
            ]
        }
        url = reverse('risks:risk-list')
        response = self.client.post(url, risk)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_risk(self):
        Risk.objects.create(name="Name 1", risk_type_id=self.risk_type.pk)
        Risk.objects.create(name="Name 2", risk_type_id=self.risk_type.pk)
        url = reverse('risks:risk-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('count'), 2)

    def test_retrieve_risk(self):
        risk = Risk.objects.create(name="Name", risk_type_id=self.risk_type.pk)
        url = reverse('risks:risk-detail', kwargs={'pk': risk.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('id'), risk.pk)
