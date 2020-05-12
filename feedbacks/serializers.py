from rest_framework import serializers
from django.conf import settings
from .models import Feedback

MAX_FEEDBACK_LENGTH = settings.MAX_FEEDBACK_LENGTH

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['id', 'content']

    def validate_content(self, value):
        if len(value) > MAX_FEEDBACK_LENGTH:
            raise serializers.ValidationError("This tweet is too long")
        return value