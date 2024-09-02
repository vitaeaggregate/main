from django.http import JsonResponse
from rest_framework import viewsets
from ..models.comment import Comment
from ..models.comment import Header
from ..serializers.comment import CommentSerializer
from rest_framework.exceptions import PermissionDenied


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        resume_pk = self.kwargs.get('resume_pk')
        member_pk = self.kwargs.get('member_pk')

        try:
            header = Header.objects.get(id=resume_pk)
        except Header.DoesNotExist:
            return JsonResponse({"detail": "Resume not found."}, status=404)
        
        comments = Comment.objects.filter(resume_id=resume_pk)

        if not comments.exists():
            return comments

        if header.is_shareable == True:
            return comments
        elif member_pk == self.request.account.get("id"):
            return comments
        else:
            raise PermissionDenied("You Don't have the permission to see these comments.")
        
        