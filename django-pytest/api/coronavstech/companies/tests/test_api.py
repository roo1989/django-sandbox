import json
import pytest
from django.urls import reverse

from companies.models import Company

companies_url = reverse("companies-list")

@pytest.mark.django_db
def test_zero_companies_should_return_an_empty_list(client) -> None:
    response = client.get(companies_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []

@pytest.mark.django_db
def test_one_company_exists_should_succeed(client) -> None:
    test_company = Company.objects.create(name="Amazon")
    response = client.get(companies_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code, 200
    assert response_content.get("name") == test_company.name
    assert response_content.get("status") == Company.CompanyStatus.HIRING
    assert response_content.get("application_link") == ""
    assert response_content.get("notes") == ""

    test_company.delete()

@pytest.mark.django_db
def test_create_company_without_arguments_should_fail(client) -> None:
    response = client.post(companies_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {"name": ["This field is required."]}

@pytest.mark.django_db
def test_create_existing_company_should_fail(client) -> None:
    Company.objects.create(name="Amazon")
    post_response = client.post(companies_url, data={"name": "Amazon"})
    assert post_response.status_code == 400
    assert json.loads(post_response.content) == {"name": ["company with this name already exists."]}

@pytest.mark.django_db
def test_create_company_only_with_name_all_fields_should_default_to_model_defaults(client) -> None:
    post_response = client.post(companies_url, data={"name": "Google"})
    post_response_json = json.loads(post_response.content)
    assert post_response.status_code ==  201
    assert post_response_json.get("name") == "Google"
    assert post_response_json.get("status") == Company.CompanyStatus.HIRING
    assert post_response_json.get("application_link") == ""
    assert post_response_json.get("notes") == ""

@pytest.mark.django_db
def test_create_company_with_layoff_status_should_succeed(client) -> None:
    post_response = client.post(companies_url, data={"name": "Test company", "status": Company.CompanyStatus.LAYOFFS})
    post_response_json = json.loads(post_response.content)
    assert post_response.status_code == 201
    assert post_response_json.get("status") == Company.CompanyStatus.LAYOFFS

@pytest.mark.django_db
def test_create_company_with_wrong_status_should_fail(client) -> None:
    post_response = client.post(companies_url, data={"name": "Test company 2", "status": "WrongStatus"})
    assert post_response.status_code == 400
    assert "WrongStatus" in str(post_response.content)
    assert "is not a valid choice" in str(post_response.content)

@pytest.mark.xfail
def test_should_be_ok_if_fails() -> None:
    assert 1 == 2

@pytest.mark.skip
def test_should_be_skipped() -> None:
    assert 1 == 2