from chat.models import Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    sender_name = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = '__all__'

    def get_sender_name(self, instance):
        return instance.sender.first_name + ' ' + instance.sender.last_name
