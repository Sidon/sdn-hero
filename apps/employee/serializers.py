from rest_framework import serializers
from apps.employee.models import Employee
from apps.company.serializers import CompanySerializer


class EmployeeSerializer(serializers.ModelSerializer):
    companies = CompanySerializer(read_only=False, many=True)

    class Meta:
        model = Employee
        fields = ('id', 'full_name', 'email', 'companies')


