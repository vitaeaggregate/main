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
    personal_info = PersonalInfoSerializer(many=False, read_only=True)
    links = LinkSerializer(many=True, read_only=True)
    awards = AwardSerializer(many=True, read_only=True)
    certificates = CertificateSerializer(many=True, read_only=True)
    courses = CourseSerializer(many=True, read_only=True)
    education_exps = EducationExpSerializer(many=True, read_only=True)
    interests = InterestSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)
    professional_exps = ProfessionalExpSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    publications = PublicationSerializer(many=True, read_only=True)
    references = ReferenceSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

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

    def to_representation(self, instance):
        representation = super().to_representation(instance)



        return representation

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
            if data_list is not None:
                for data in data_list:
                    model.objects.create(header=header, **data)

        header = Header.objects.create(**validated_data)

        return header

    def update(self, instance, validated_data):
        personal_info_data = validated_data.pop("personal_info", None)
        links_data = validated_data.pop("links", None)
        awards_data = validated_data.pop("awards", None)
        certificates_data = validated_data.pop("certificates", None)
        courses_data = validated_data.pop("courses", None)
        education_exps_data = validated_data.pop("education_exps", None)
        interests_data = validated_data.pop("interests", None)
        languages_data = validated_data.pop("languages", None)
        professional_exps_data = validated_data.pop("professional_exps", None)
        projects_data = validated_data.pop("projects", None)
        publications_data = validated_data.pop("publications", None)
        skills_data = validated_data.pop("skills", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if personal_info_data:
            PersonalInfo.objects.update_or_create(header=instance, defaults=personal_info_data)

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
            if data_list is not None:
                for data in data_list:
                    model.objects.update_or_create(header=instance, defaults=data)

        instance.save()

        return instance