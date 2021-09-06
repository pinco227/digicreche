from rest_framework import serializers
from schools.models import School


class SchoolSerializer(serializers.ModelSerializer):
    manager = serializers.StringRelatedField(read_only=True)
    rooms_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = '__all__'

    def get_rooms_count(self, instance):
        return instance.rooms.count()
