from rest_framework import viewsets, filters
from rest_framework.authentication import BaseAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from aluraflix.models import Program
from aluraflix.serializers import ProgramSerializer


# Create your views here.
class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    
    serializer_class = ProgramSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["title"]
    filterset_fields = ['type']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]