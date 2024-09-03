from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views.account import AccountViewSet
from .resume.views.header import HeaderViewSet
# from .resume.views.personal_info import PersonalInfoViewSet
# from .resume.views.link import LinkViewSet
# from .resume.views.professional_exp import ProfessionalExpViewSet
# from .resume.views.education_exp import EducationExpViewSet
# from .resume.views.reference import ReferenceViewSet
# from .resume.views.certificate import CertificateViewSet
# from .resume.views.award import AwardViewSet
# from .resume.views.language import LanguageViewSet
# from .resume.views.project import ProjectViewSet
# from .resume.views.skill import SkillViewSet
# from .resume.views.course import CourseViewSet
# from .resume.views.publication import PublicationViewSet
# from .resume.views.interest import InterestViewSet
from .resume.views.comment import CommentViewSet

# views = {
#     "interests": InterestViewSet,
#     "publications": PublicationViewSet,
#     "skills": SkillViewSet,
#     "educations": EducationExpViewSet,
#     "personal-infos": PersonalInfoViewSet,
#     "links": LinkViewSet,
#     "professional-exps": ProfessionalExpViewSet,
#     "references": ReferenceViewSet,
#     "projects": ProjectViewSet,
#     "courses": CourseViewSet,
#     "certificates": CertificateViewSet,
#     "awards": AwardViewSet,
#     "languages": LanguageViewSet,
#     "comments": CommentViewSet
# }

router = DefaultRouter()

# for route in views:
#     router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/" + route,
#                     views[route], basename="view " + route + " by resume id ")
#     router.register(r"members/(?P<member_pk>[^/.]+)/resumes/" + route,
#                     views[route], basename="view all " + route + " from all resumes from a member")
#     router.register(r"members/resumes/" + route,
#                     views[route], basename="view all " + route)


# Resume Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes",
                HeaderViewSet, basename="view resumes by member id")
router.register(r"members/resumes", HeaderViewSet, basename="view all resumes")
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)",
                HeaderViewSet, basename="view certain resume of a member by resume id")

# Comment Route
router.register(r"members/(?P<member_pk>[^/.]+)/resumes/(?P<resume_pk>[^/.]+)/comments",
                CommentViewSet, basename="view comments by member id and resume id")
router.register(r"members/(?P<member_pk>[^/.]+)/comments",
                CommentViewSet, basename="view comments by member id")

# Member Route
router.register(r"members", AccountViewSet)

urlpatterns = [
    path("", include(router.urls))
]
