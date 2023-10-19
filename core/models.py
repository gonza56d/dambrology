from datetime import date

from pydantic import BaseModel as PydanticModel

from core.exceptions import InvalidInput


class Numerology(PydanticModel):

    essence: int
    image: int
    destiny: int
    path: int
    present_numbers: list[int] = []
    missing_numbers: list[int] = []


class Person(PydanticModel):

    first_name: str
    last_name: str
    birth: date
    numerology: Numerology | None = None

    def __init__(self, **kwargs):
        kwargs = self._clean_for_utf8(kwargs)
        super().__init__(**kwargs)
        self._validate_ascii((self.first_name + self.last_name))

    def _validate_ascii(self, names: str):
        try:
            names.encode('ascii')
        except UnicodeError:
            raise InvalidInput('Name must contain only utf-8 characters')

    def _clean_for_utf8(self, kwargs: dict) -> dict:
        kwargs['first_name'] = self._replace_for_utf8(kwargs['first_name'])
        kwargs['last_name'] = self._replace_for_utf8(kwargs['last_name'])
        return kwargs

    def _replace_for_utf8(self, value: str) -> str:
        if not value:
            return value
        return value.lower().replace('ñ', 'n')\
            .replace('á', 'a')\
            .replace('é', 'e')\
            .replace('í', 'i')\
            .replace('ó', 'o')\
            .replace('ú', 'u')


class NumerologyStudyData:

    _VOWELS = ('a', 'e', 'i', 'o', 'u')

    def __init__(self, person: Person) -> None:
        self.name_complete = [*person.first_name.split(' '), *person.last_name.split(' ')]

        self.name_vowels: list[str] = [
            ''.join(letter for letter in name if letter in self._VOWELS)
            for name in self.name_complete
        ]
        self.name_consonants: list[str] = [
            ''.join(letter for letter in name if letter not in self._VOWELS)
            for name in self.name_complete
        ]
