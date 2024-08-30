from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.education_exp import EducationExpViewSet

router = DefaultRouter()
router.register(r"members/resumes/education-exp",
                EducationExpViewSet, basename="view all education experience")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/education-exp",
                EducationExpViewSet, basename="view educational experience by member")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/education-exp",
                EducationExpViewSet, basename="view all education experience by resume id")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")
router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")
router.register(r"members", AccountViewSet)
