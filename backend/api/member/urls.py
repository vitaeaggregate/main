from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.personal_info import PersonalInfoViewSet

router = DefaultRouter()
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/personal-infos",
                PersonalInfoViewSet, basename="view personal info from by resume id ")

router.register(r"members/(?P<member_pk>[^/.]+)/resumes/personal-infos",
                PersonalInfoViewSet, basename="view all personal info from all resumes from a member")

router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")

router.register(r"members/resumes/personal-info",
                PersonalInfoViewSet, basename="view all personal-infos")

router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")

router.register(r"members", AccountViewSet)
