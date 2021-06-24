from django.db.models import fields
from rest_framework import serializers
from keci.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id','title','created_by','abstract','language','status','branches','document')