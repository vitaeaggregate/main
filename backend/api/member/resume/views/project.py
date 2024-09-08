from rest_framework import viewsets
from ..models.project import Project
from ..serializers.project import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get("header_pk")
        if (header_pk):
            return Project.objects.filter(header_id=header_pk)
        return Project.objects.all()
