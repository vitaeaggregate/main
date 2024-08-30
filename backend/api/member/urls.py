from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
from .resume.views.personal_info import PersonalInfoViewSet
from .resume.views.link import LinkViewSet
from .resume.views.professional_exp import ProfessionalExpViewSet
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

# Resume Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")
router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")

# Member Route
router.register(r"members", AccountViewSet)
