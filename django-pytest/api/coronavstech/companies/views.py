from django.core.mail import send_mail
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from companies.models import Company
from companies.serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination

@api_view(http_method_names=["POST"])
def send_company_email(request: Request) -> Response:
    send_mail(subject="My cool subject", message="My cool message", from_email="ragnar.orn@gmail.com", recipient_list=["ragnar.orn@gmail.com"])
    return Response({"status": "Success", "info": "Email sent successfully", "status": 200})