from rest_framework import viewsets
from .models import MyModel
from .serializers import Myserializer


class MyView(viewsets.ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = Myserializer
