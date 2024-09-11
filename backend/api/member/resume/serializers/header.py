from rest_framework import serializers
from api.member.models.account import Account
from ..models.header import Header
from .personal_info import PersonalInfoSerializer, PersonalInfo
from .link import LinkSerializer, Link
from .award import AwardSerializer, Award
from .certificate import CertificateSerializer, Certificate
from .course import CourseSerializer, Course
from .education import EducationSerializer, Education
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
    educations = EducationSerializer(many=True, required=False)
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
            "educations",
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

    def create(self, validated_data):
        header = Header.objects.create(
            member=validated_data.pop("member"), title=validated_data.pop("title"), is_shareable=validated_data.pop("is_shareable"))

        PersonalInfo.objects.create(
            header=header, **validated_data.pop("personal_info", []))

        model_data_mapping = {
            Link: validated_data.pop("links", []),
            Award: validated_data.pop("awards", []),
            Certificate: validated_data.pop("certificates", []),
            Course: validated_data.pop("courses", []),
            Education: validated_data.pop("educations", []),
            Interest: validated_data.pop("interests", []),
            Language: validated_data.pop("languages", []),
            ProfessionalExp: validated_data.pop("professional_exp", []),
            Project: validated_data.pop("projects", []),
            Publication: validated_data.pop("publications", []),
            Skill: validated_data.pop("skills", []),
            Reference: validated_data.pop("references", []),
        }

        for model, data_list in model_data_mapping.items():
            if data_list is not []:
                for data in data_list:
                    model.objects.create(header=header, **data)

        return header

    def update(self, instance, validated_data):
        instance.member = validated_data.get('member', instance.member)
        instance.title = validated_data.get('title', instance.title)
        instance.is_shareable = validated_data.get(
            'is_shareable', instance.is_shareable)
        instance.save()

        PersonalInfo.objects.update(**validated_data.pop("personal_info"))

        model_data_mapping = {
            Link: validated_data.pop("links", []),
            Award: validated_data.pop("awards", []),
            Certificate: validated_data.pop("certificates", []),
            Course: validated_data.pop("courses", []),
            Education: validated_data.pop("educations", []),
            Interest: validated_data.pop("interests", []),
            Language: validated_data.pop("languages", []),
            ProfessionalExp: validated_data.pop("professional_exp", []),
            Project: validated_data.pop("projects", []),
            Publication: validated_data.pop("publications", []),
            Skill: validated_data.pop("skills", []),
            Reference: validated_data.pop("references", []),
        }

        for model, data_list in model_data_mapping.items():
            objects = model.objects.filter(header_id=instance.id)
            for object in objects:
                is_included = False
                for data in data_list:
                    if data.get("id") and int(data.get("id")) == object.id:
                        is_included = True
                        break
                if not is_included:
                    object.delete()

            for data in data_list:
                if (isinstance(data.get("id"), int)):
                    data_id = int(data.get("id"))
                    object = model.objects.filter(id=data_id).first()
                    if object:
                        model.objects.update_or_create(
                            id=data_id, header=instance, defaults=data)
                else:
                    model.objects.create(header_id=instance.id, **data)

        return instance
