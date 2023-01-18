import json
from unittest import TestCase
from django.test import Client
from django.urls import reverse


class TestGetCompanies(TestCase):
    def test_zero_companies_should_return_an_empty_list(self):
        client = Client()
        response = client.get(reverse("companies-list"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])