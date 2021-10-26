from activities.models import Activity, ActivityImage, ActivityType
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import serializers


class ActivityTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityType
        fields = '__all__'


class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = ('image',)


class ActivitySerializer(serializers.ModelSerializer):
    """ CREDIT https://www.py4u.net/discuss/192406 """

    images = ActivityImageSerializer(many=True, read_only=True)

    def __init__(self, *args, **kwargs):
        file_fields = kwargs.pop('file_fields', None)
        super().__init__(*args, **kwargs)
        if file_fields:
            field_update_dict = {field: serializers.FileField(
                required=False, write_only=True) for field in file_fields}
            self.fields.update(**field_update_dict)

    def create(self, validated_data):
        validated_data_copy = validated_data.copy()
        validated_files = []
        for key, value in validated_data_copy.items():
            if isinstance(value, InMemoryUploadedFile):
                validated_files.append(value)
                validated_data.pop(key)
        activity_instance = super().create(validated_data)
        for image in validated_files:
            ActivityImage.objects.create(
                activity=activity_instance, image=image)
        return activity_instance

    class Meta:
        model = Activity
        exclude = ['pupil']
