from rest_framework import viewsets
from ..models.comment import Comment
from ..serializers.comment import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get('resume_pk')
        if resume_pk:
            return Comment.objects.filter(resume_id=resume_pk)
        return Comment.objects.all()
