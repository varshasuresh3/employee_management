from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeePagination(PageNumberPagination):
    page_size = 10

class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['department', 'role']

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer