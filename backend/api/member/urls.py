from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.personal_info import PersonalInfoViewSet
from .resume.views.link import LinkViewSet
from .resume.views.professional_exp import ProfessionalExpViewSet
from .resume.views.education_exp import EducationExpViewSet
from .resume.views.project import ProjectViewSet

router = DefaultRouter()
# Two routes here for each table

# Project Route
router.register(r"members/resumes/projects",
                ProjectViewSet, basename="view all projects")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/projects",
                ProjectViewSet, basename="view projects by member")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/projects",
                ProjectViewSet, basename="view all projects by resume id")

# Education Exp Route
router.register(r"members/resumes/education-exp",
                EducationExpViewSet, basename="view all education experience")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/education-exp",
                EducationExpViewSet, basename="view education experience by member")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/education-exp",
                EducationExpViewSet, basename="view all education experience by resume id")

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
