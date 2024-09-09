from rest_framework import serializers
from ..models.course import Course


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Course
        exclude = ["header"]
