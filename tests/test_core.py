from datetime import date
from unittest import TestCase

import pytest

from core.calculation import calculate_number, get_present_and_missing_numbers, make_numerology, reduce_number
from core.exceptions import InvalidInput
from core.models import Numerology, NumerologyStudyData, Person


class TestNumerologyStudyData(TestCase):

    def setUp(self) -> None:
        self.person = Person(first_name='Gonzalo Manuel', last_name='Dambra', birth=date(1996, 7, 1))

    def test_study_data(self):
        study_data = NumerologyStudyData(self.person)
        assert study_data.name_vowels == ['oao', 'aue', 'aa']
        assert study_data.name_consonants == ['gnzl', 'mnl', 'dmbr']
        assert study_data.name_complete == ['gonzalo', 'manuel', 'dambra']

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

    @pytest.mark.parametrize(
        'person, expected_numerology',
        [
            (
                Person(first_name='Gonzalo Manuel', last_name='Dambra', birth=date(1996, 7, 1)),
                Numerology(
                    essence=6,
                    image=9,
                    destiny=6,
                    path=6,
                    present_numbers=[7, 6, 5, 8, 1, 3, 6, 4, 1, 5, 3, 5, 3, 4, 1, 4, 2, 9, 1],
                    missing_numbers=[]
                )
            ),
            (
                Person(first_name='Victor Daniel', last_name='Dambra', birth=date(1956, 5, 15)),
                Numerology(
                    essence=5,
                    image=4,
                    destiny=9,
                    path=5,
                    present_numbers=[4, 9, 3, 2, 6, 9, 4, 1, 5, 9, 5, 3, 4, 1, 4, 2, 9, 1],
                    missing_numbers=[7, 8]
                )
            ),
            (
                Person(first_name='Lujan Victoria', last_name='Garcia', birth=date(2011, 7, 22)),
                Numerology(
                    essence=22,
                    image=1,
                    destiny=5,
                    path=33,
                    present_numbers=[3, 3, 1, 1, 5, 4, 9, 3, 2, 6, 9, 9, 1, 7, 1, 9, 3, 9, 1],
                    missing_numbers=[8]
                )
            ),
        ]
    )
    def test_make_numerology(self, person: Person, expected_numerology: Numerology):
        result = make_numerology(person)
        assert result.numerology == expected_numerology


class TestNumbersAndMissing:

    @pytest.mark.parametrize(
        'full_name, expected_numbers, expected_missing',
        [
            ('Gonzalo Manuel Dambra', [7, 6, 5, 8, 1, 3, 6, 4, 1, 5, 3, 5, 3, 4, 1, 4, 2, 9, 1], []),
            ('Pepe Juan Perez', [7, 5, 7, 5, 1, 3, 1, 5, 7, 5, 9, 5, 8], [2, 4, 6]),
            ('Alexi Laiho', [1, 3, 5, 6, 9, 3, 1, 9, 8, 6], [2, 4, 7])
        ]
    )
    def test_get_present_and_missing_numbers(self, full_name: str, expected_numbers: list[int], expected_missing: list[int]):
        results = get_present_and_missing_numbers(full_name)
        assert results[0] == expected_numbers
        assert results[1] == expected_missing
