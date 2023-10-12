from unittest import TestCase

from core.exceptions import InvalidInput
from core.models import NumerologyStudyData, Person


class TestNumerologyStudyData(TestCase):

    def setUp(self) -> None:
        self.person = Person(first_name='Gonzalo Manuel', last_name='Dambra')

    def test_study_data(self):
        study_data = NumerologyStudyData(self.person)
        assert study_data._name_vowels == ['oao', 'aue', 'aa']
        assert study_data._name_consonants == ['gnzl', 'mnl', 'dmbr']
        assert study_data._name_complete == ['gonzalo', 'manuel', 'dambra']

    def test_invalid_name(self):
        with self.assertRaises(InvalidInput):
            Person(first_name='Gön', last_name='Sómething')

    def test_valid_name_with_accents(self):
        person = Person(first_name='Gón', last_name='Sómething')
        assert person.first_name == 'gon'
        assert person.last_name == 'something'
