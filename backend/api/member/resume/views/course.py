from rest_framework import viewsets
from ..models.course import Course
from ..serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get('resume_pk')
        if resume_pk:
            return Course.objects.filter(resume_id=resume_pk)
        return Course.objects.all()
