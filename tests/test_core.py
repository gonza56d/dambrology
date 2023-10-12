from datetime import date
from unittest import TestCase

import pytest

from core.calculation import calculate_number, reduce_number
from core.exceptions import InvalidInput
from core.models import NumerologyStudyData, Person


class TestNumerologyStudyData(TestCase):

    def setUp(self) -> None:
        self.person = Person(first_name='Gonzalo Manuel', last_name='Dambra', birth=date(1996, 7, 1))

    def test_study_data(self):
        study_data = NumerologyStudyData(self.person)
        assert study_data._name_vowels == ['oao', 'aue', 'aa']
        assert study_data._name_consonants == ['gnzl', 'mnl', 'dmbr']
        assert study_data._name_complete == ['gonzalo', 'manuel', 'dambra']

    def test_invalid_name(self):
        with self.assertRaises(InvalidInput):
            Person(first_name='Gön', last_name='Sómething', birth=date(2000, 1, 1))
        with self.assertRaises(InvalidInput):
            Person(first_name='Gon', last_name='Sömething', birth=date(2000, 1, 1))

    def test_valid_name_with_accents(self):
        person = Person(first_name='Góñ', last_name='Sómething', birth=date(2000, 1, 1))
        assert person.first_name == 'gon'
        assert person.last_name == 'something'


class TestCalculation:

    @pytest.mark.parametrize(
        'word, expected_result',
        [('gonzalo', 9), ('manuel', 3), ('garcia', 3), ('dambra', 3), ('aia', 11)]
    )
    def test_calculate_number(self, word: str, expected_result: int):
        result = calculate_number(word)
        assert result == expected_result

    @pytest.mark.parametrize(
        'number, expected_result',
        [(9, 9), (1, 1), (11, 11), (22, 22), (33, 33), (12, 3), (23, 5), (10, 1), (20, 2), (6, 6)]
    )
    def test_reduce_number(self, number: int, expected_result: int):
        result = reduce_number(number)
        assert result == expected_result
