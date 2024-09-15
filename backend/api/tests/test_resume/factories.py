import factory
from ...member.resume.models.personal_info import PersonalInfo
from ...member.resume.models.language import Language


class PersonalInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PersonalInfo
    full_name = "test"
    job_title = "testJob"
    email = "test@test.com"
    phone_number = "00000000000"
    address = "123 test lane"
    date_of_birth = "01/01/2024"
    driving_license = "test"
    gender_pronoun = "test/tester"
    marital_status = "test"
    nationality = "principality of test"


class LanguageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Language
    language = "test"
    description = "test test"
    skill_level = "test test test"
