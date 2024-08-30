from rest_framework import viewsets
from ..models.project import Project
from ..serializers.project import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get("resume_pk")
        if (resume_pk):
            return Project.objects.filter(resume_id=resume_pk)
        return Project.objects.all()
