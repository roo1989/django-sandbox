from rest_framework.routers import DefaultRouter

from companies.views import CompanyViewSet

companies_router = DefaultRouter()
companies_router.register("companies", viewset=CompanyViewSet, basename="companies")