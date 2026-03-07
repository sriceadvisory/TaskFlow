from django.utils import timezone
from rest_framework import serializers
from .models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('id', 'title', 'description', 'completed', 'priority', 'due_date')

    def create(self, validated_data):
         request = self.context["request"]
         validated_data['owner'] = request.user
         return super().create(validated_data)

    def validate_priority(self, value):
            if not (1 <= value <= 5):
                raise serializers.ValidationError("Priority must be 1-5.")
            return value
    
    def validate_due_date(self, value):
         if value <= timezone.now().date():
              raise serializers.ValidationError("Due date must be in the future")
         return value