from rest_framework import viewsets
from ..models.language import Language
from ..serializers.language import LanguageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get('header_pk')
        if header_pk:
            return Language.objects.filter(header_id=header_pk)
        return Language.objects.all()
