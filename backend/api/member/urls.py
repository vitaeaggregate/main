from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.personal_info import PersonalInfoViewSet
from .resume.views.link import LinkViewSet
from .resume.views.professional_exp import ProfessionalExpViewSet
<<<<<<< HEAD
from .resume.views.certificate import Certificate

router = DefaultRouter()

# Two routes here for each table

# Professional Exp Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/professional-exp",
                ProfessionalExpViewSet, basename="view professional exp from by resume id ")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/professional-exp",
                ProfessionalExpViewSet, basename="view all professional exp from all resumes from a member")
router.register(r"members/resumes/professional-exp",
                ProfessionalExpViewSet, basename="view all professional exp")

# Certificate Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/certificates",
                Certificate, basename="view professional exp from by resume id ")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/certificates",
                Certificate, basename="view all professional exp from all resumes from a member")
router.register(r"members/resumes/certificates",
                Certificate, basename="view all professional exp")

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
=======
from .resume.views.education_exp import EducationExpViewSet
from .resume.views.reference import ReferenceViewSet

views = {
    "education": EducationExpViewSet,
    "personal-infos": PersonalInfoViewSet,
    "links": LinkViewSet,
    "professional-exps": ProfessionalExpViewSet,
    "references": ReferenceViewSet
}

router = DefaultRouter()

for route in views:
    router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/" + route,
                    views[route], basename="view " + route + " by resume id ")
    router.register(r"members/(?P<member_pk>[^/.]+)/resumes/" + route,
                    views[route], basename="view all " + route + " from all resumes from a member")
    router.register(r"members/resumes/" + route,
                    views[route], basename="view all " + route)
>>>>>>> b6ce996431a0b265ccba7c9ee02fb6ad0cab7c61

# Resume Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")
router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")

# Member Route
router.register(r"members", AccountViewSet)
