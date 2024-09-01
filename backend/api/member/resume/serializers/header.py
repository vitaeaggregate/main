from rest_framework import serializers
from ..models.header import Header

from .personal_info import PersonalInfoSerializer, PersonalInfo
from .link import LinkSerializer, Link
from .award import AwardSerializer, Award
from .certificate import CertificateSerializer, Certificate
from .course import CourseSerializer, Course
from .education_exp import EducationExpSerializer, EducationExp
from .interest import InterestSerializer, Interest
from .language import LanguageSerializer, Language
from .professional_exp import ProfessionalExpSerializer, ProfessionalExp
from .project import ProjectSerializer, Project
from .publication import PublicationSerializer, Publication
from .reference import ReferenceSerializer, Reference
from .skill import SkillSerializer, Skill


class HeaderSerializer(serializers.ModelSerializer):
    personal_info = PersonalInfoSerializer(many=False, read_only=False)
    links = LinkSerializer(many=True, read_only=False)
    awards = AwardSerializer(many=True, read_only=False)
    certificates = CertificateSerializer(many=True, read_only=False)
    courses = CourseSerializer(many=True, read_only=False)
    education_exps = EducationExpSerializer(many=True, read_only=False)
    interests = InterestSerializer(many=True, read_only=False)
    languages = LanguageSerializer(many=True, read_only=False)
    professional_exps = ProfessionalExpSerializer(many=True, read_only=False)
    projects = ProjectSerializer(many=True, read_only=False)
    publications = PublicationSerializer(many=True, read_only=False)
    references = ReferenceSerializer(many=True, read_only=False)
    skills = SkillSerializer(many=True, read_only=False)

    class Meta:
        model = Header
        fields = [
            "id",
            "member",
            "title",
            "personal_info",
            "links",
            "awards",
            "certificates",
            "courses",
            "education_exps",
            "interests",
            "languages",
            "professional_exps",
            "projects",
            "publications",
            "references",
            "skills",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        personal_info_data = validated_data.pop("personal_info")
        links_data = validated_data.pop("links")
        awards_data = validated_data.pop("awards")
        certificates_data = validated_data.pop("certificates")
        courses_data = validated_data.pop("courses")
        education_exps_data = validated_data.pop("educations_exps")
        interests_data = validated_data.pop("interests")
        languages_data = validated_data.pop("languages")
        professional_exps_data = validated_data.pop("professional_exp")
        projects_data = validated_data.pop("projects")
        publications_data = validated_data.pop("publications")
        skills_data = validated_data.pop("skills")

        PersonalInfo.objects.create(header=header, **personal_info_data)

        model_data_mapping = {
            Link: links_data,
            Award: awards_data,
            Certificate: certificates_data,
            Course: courses_data,
            EducationExp: education_exps_data,
            Interest: interests_data,
            Language: languages_data,
            ProfessionalExp: professional_exps_data,
            Project: projects_data,
            Publication: publications_data,
            Skill: skills_data
        }

        for model, data_list in model_data_mapping.items():
            for data in data_list:
                model.objects.create(header=header, **data)

        header = Header.objects.create(**validated_data)

        return header
