from django.db.models.fields import SlugField
from rest_framework import generics
from keci.models import Project
from .serializers import ProjectSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.projectobjects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    lookup_field = 'id'

