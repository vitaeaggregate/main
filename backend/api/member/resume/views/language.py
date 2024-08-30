from rest_framework import viewsets
from ..models.language import Language
from ..serializers.language import LanguageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get('resume_pk')
        if resume_pk:
            return Language.objects.filter(resume_id=resume_pk)
        return Language.objects.all()
