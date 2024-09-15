from pytest_factoryboy import register

from .factories import LanguageFactory, PersonalInfoFactory

register(LanguageFactory)
register(PersonalInfoFactory)