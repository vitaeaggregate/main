from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.professional_exp import ProfessionalExpViewSet

router = DefaultRouter()

router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/professional-exp",
                ProfessionalExpViewSet, basename="view professional exp from by resume id ")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/professional-exp",
                ProfessionalExpViewSet, basename="view all professional exp from all resumes from a member")

router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")
router.register(r"members/resumes/professional-exp",
                ProfessionalExpViewSet, basename="view all professional exp")
router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")
router.register(r"members", AccountViewSet)
