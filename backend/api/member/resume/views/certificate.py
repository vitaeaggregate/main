from rest_framework import viewsets
from ..models.certificate import Certificate
from ..serializers.certificate import CertificateSerializer


class CertificateViewSet(viewsets.ModelViewSet):
    serializer_class = CertificateSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get('resume_pk')
        if resume_pk:
            return Certificate.objects.filter(resume_id=resume_pk)
        return Certificate.objects.all()
