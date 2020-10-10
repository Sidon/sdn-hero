from rest_framework import serializers
from apps.company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'cnpj', 'uf')

    # def create(self, validated_data):
    #     company = Company.objects.create(**validated_data)
    #     return company
