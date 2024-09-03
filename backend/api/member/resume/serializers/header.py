from rest_framework import serializers
from api.member.models.account import Account
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
    professional_exps = ProfessionalExpSerializer(many=True, required=False)
    personal_info = PersonalInfoSerializer(many=False, required=False)
    education_exps = EducationExpSerializer(many=True, required=False)
    publications = PublicationSerializer(many=True, required=False)
    certificates = CertificateSerializer(many=True, required=False)
    references = ReferenceSerializer(many=True, required=False)
    interests = InterestSerializer(many=True, required=False)
    languages = LanguageSerializer(many=True, required=False)
    projects = ProjectSerializer(many=True, required=False)
    courses = CourseSerializer(many=True, required=False)
    awards = AwardSerializer(many=True, required=False)
    skills = SkillSerializer(many=True, required=False)
    links = LinkSerializer(many=True, required=False)

    class Meta:
        model = Header
        fields = [
            "id",
            "member",
            "title",
            "is_shareable",
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

        request = self.context.get("request")

        if not request.account.get("id") == instance.member.id and instance.is_shareable == True:

            sensitive_fields = [
                "member",
                "personal_info",
                "links",
                "projects",
                "publications",
                "references",
            ]

            for field in sensitive_fields:
                if field in representation:
                    representation.pop(field)
            return representation

        if request.account.get("id") == instance.member.id:
            return representation

        return {field: representation[field] for field in ["id", "is_shareable"]}

    def removeAllHeaders(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                if "header" in value:
                    del value["header"]
            elif isinstance(value, list):
                for item in value:
                    if "header" in item:
                        del item["header"]
        return data

    def create(self, validated_data):
        validated_data = self.removeAllHeaders(validated_data)

        member_data = validated_data.pop("member")
        title_data = validated_data.pop("title")
        
        if "is_shareable" in validated_data:
            is_shareable_data = validated_data.pop("is_shareable")

        header = Header.objects.create(member=member_data, title=title_data, is_shareable=is_shareable_data)

        personal_info_data = validated_data.pop("personal_info", None)
        links_data = validated_data.pop("links", None)
        awards_data = validated_data.pop("awards", None)
        certificates_data = validated_data.pop("certificates", None)
        courses_data = validated_data.pop("courses", None)
        education_exps_data = validated_data.pop("education_exps", None)
        interests_data = validated_data.pop("interests", None)
        languages_data = validated_data.pop("languages", None)
        professional_exps_data = validated_data.pop("professional_exp", None)
        projects_data = validated_data.pop("projects", None)
        publications_data = validated_data.pop("publications", None)
        skills_data = validated_data.pop("skills", None)
        references_data = validated_data.pop("references", None)

        if personal_info_data:
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
            Skill: skills_data,
            Reference: references_data,
        }

        for model, data_list in model_data_mapping.items():
            if data_list is not None:
                for data in data_list:
                    model.objects.create(header=header, **data)

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
            PersonalInfo.objects.update_or_create(
                header=instance, defaults=personal_info_data)

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
                    model.objects.update_or_create(
                        header=instance, defaults=data)

        instance.save(update_fields=["updated_at"])

        return instance
