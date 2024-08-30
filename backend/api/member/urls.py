from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.personal_info import PersonalInfoViewSet
from .resume.views.link import LinkViewSet
from .resume.views.professional_exp import ProfessionalExpViewSet

router = DefaultRouter()

# Two routes here for each table

# Professional Exp Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/professional-exp",
                ProfessionalExpViewSet, basename="view professional exp from by resume id ")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/professional-exp",
                ProfessionalExpViewSet, basename="view all professional exp from all resumes from a member")
router.register(r"members/resumes/professional-exp",
                ProfessionalExpViewSet, basename="view all professional exp")

# Link Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/links",
                LinkViewSet, basename="view link by resume id ")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/links",
                LinkViewSet, basename="view all links from all resumes from a member")

# Personal Info Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/personal-infos",
                PersonalInfoViewSet, basename="view personal info by resume id ")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/personal-infos",
                PersonalInfoViewSet, basename="view all personal infos from all resumes from a member")

# Resume Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")

# View All from everything here
router.register(r"members/resumes/links",
                LinkViewSet, basename="view all links")
router.register(r"members/resumes/personal-infos",
                PersonalInfoViewSet, basename="view all personal infos")
router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")
router.register(r"members", AccountViewSet)
