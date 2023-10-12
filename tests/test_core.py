from unittest import TestCase

from core.models import NumerologyStudyData, Person


class TestNumerologyStudyData(TestCase):

    def test_study_data(self):
        person = Person(first_name='Gonzalo Manuel', last_name='Dambra')
        study_data = NumerologyStudyData(person)
        assert study_data._name_vowels == ['oao', 'aue', 'aa']
        assert study_data._name_consonants == ['gnzl', 'mnl', 'dmbr']
        assert study_data._name_complete == ['gonzalo', 'manuel', 'dambra']
