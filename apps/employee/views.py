from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView
from rest_framework import mixins
from .serializers import EmployeeSerializer
from .models import Employee


class EmployeeViewSet(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    permission_classes = (AllowAny,)
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
