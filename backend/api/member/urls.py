from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.education_exp import EducationExpViewSet

router = DefaultRouter()
router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")
router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")
router.register(r"members", AccountViewSet)
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/educational-exp",
                EducationExpViewSet, basename="view all educational experience by resume id")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/educational-exp/(?P<id_pk>[^/.]+)",
                EducationExpViewSet, basename="view educational experience by educational experience id ")
