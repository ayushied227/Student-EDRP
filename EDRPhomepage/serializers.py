from rest_framework import serializers
from .models import Student, Subject

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student, Subject
        fields= '__all__'
    