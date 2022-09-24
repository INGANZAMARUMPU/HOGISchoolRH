from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters

from .models import *
from .serializers import *

class TokenPairView(TokenObtainPairView):
    serializer_class = TokenPairSerializer

class DeuxParPage(PageNumberPagination):
    page_size = 8
    max_page_size = 2

class NiveauViewSet(viewsets.ModelViewSet):
    queryset = Niveau.objects.all()
    serializer_class = NiveauSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    pagination_class = DeuxParPage

    filter_backends = filters.DjangoFilterBackend, SearchFilter
    search_fields = ["nom",] 
    filterset_fields = {
        'nom': ['exact', 'icontains',],
        'poid': ['gte', 'lte',],
    }

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

class PresenceViewSet(viewsets.ModelViewSet):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication, SessionAuthentication]

class CongeViewSet(viewsets.ModelViewSet):
    queryset = Conge.objects.all()
    serializer_class = CongeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication, SessionAuthentication]
