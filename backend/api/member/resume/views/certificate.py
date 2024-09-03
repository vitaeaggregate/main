from rest_framework import viewsets
from ..models.certificate import Certificate
from ..serializers.certificate import CertificateSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        header_pk = self.kwargs.get('header_pk')
        if header_pk:
            return Certificate.objects.filter(header_id=header_pk)
        return Certificate.objects.all()
