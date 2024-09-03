from rest_framework import viewsets
from ..models.course import Course
from ..serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get('header_pk')
        if header_pk:
            return Course.objects.filter(header_id=header_pk)
        return Course.objects.all()
