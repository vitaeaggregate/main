from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.comment import CommentViewSet

router = DefaultRouter()

# Comment Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<header_pk>[^/.]+)/comments",
                CommentViewSet, basename="view comments by member id and resume id")

router.register(r"members/(?P<member_pk>[^/.]+)/comments",
                CommentViewSet, basename="view comments by member id")

# Resume Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")
router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)",
                HeaderViewSet, basename="view certain resume of a member by resume id")

# Member Route
router.register(r"members", AccountViewSet)

urlpatterns = [
    path("", include(router.urls))
]
