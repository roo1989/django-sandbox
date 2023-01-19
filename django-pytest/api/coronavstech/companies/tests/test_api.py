import json
import pytest

from unittest import TestCase
from django.test import Client
from django.urls import reverse

from companies.models import Company

@pytest.mark.django_db
class BasicCompanyAPITestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.companies_url = reverse("companies-list")

    def tearDown(self) -> None:
        pass

class TestGetCompanies(BasicCompanyAPITestCase):
    def test_zero_companies_should_return_an_empty_list(self) -> None:
        response = self.client.get(self.companies_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), [])

    def test_one_company_exists_should_succeed(self) -> None:
        test_company = Company.objects.create(name="Amazon")
        response = self.client.get(self.companies_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), test_company.name)
        self.assertEqual(response_content.get("status"), "Hiring")
        self.assertEqual(response_content.get("application_link"), "")
        self.assertEqual(response_content.get("notes"), "")

        test_company.delete()

class TestPostCompanies(BasicCompanyAPITestCase):
    def test_create_company_without_arguments_should_fail(self) -> None:
        response = self.client.post(self.companies_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content), {"name": ["This field is required."]}
        )

    def test_create_existing_company_should_fail(self) -> None:
        Company.objects.create(name="Amazon")
        post_response = self.client.post(self.companies_url, data={"name": "Amazon"})
        self.assertEqual(post_response.status_code, 400)
        self.assertEqual(
            json.loads(post_response.content), {"name": ["company with this name already exists."]}
        )

    def test_create_company_only_with_name_all_fields_should_default_to_model_defaults(self) -> None:
        pass