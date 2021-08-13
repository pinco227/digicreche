from rest_framework import serializers
from schools.models import School


class SchoolSerializer(serializers.ModelSerializer):
    manager = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = School
        fields = '__all__'
