from core.models import NumerologyStudyData, Person


def make_numerology(person: Person) -> Person:
    study_data = NumerologyStudyData(person)
