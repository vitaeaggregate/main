from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.comment_notification import CommentNotificationViewSet
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.comment import CommentViewSet

router = DefaultRouter()

# Comment Route
router.register(r"members/(?P<member_pk>[^/.]+)/comments",
                CommentViewSet, basename="view comments by member id")

router.register(r"resumes/(?P<header_pk>[^/.]+)/comments",
                CommentViewSet, basename="view comments by member id and resume id")

router.register(r"comments",
                CommentViewSet, basename="view comments")
# Resume Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes of a member")
router.register(r"resumes",
                HeaderViewSet, basename="view resumes")

# Notifications Route
router.register(r"notifications/comments/receivers/(?P<member_pk>[^/.]+)",
                CommentNotificationViewSet, basename="view notifications by member id")
router.register(r"notifications/comments",
                CommentNotificationViewSet, basename="view all notifications")

# Member Route
router.register(r"members", AccountViewSet)


urlpatterns = [
    path("", include(router.urls))
]
