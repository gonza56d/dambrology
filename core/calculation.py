from core.models import NumerologyStudyData, Person


letter_number = {
    'a': 1, 'j': 1, 's': 1,
    'b': 2, 'k': 2, 't': 2,
    'c': 3, 'l': 3, 'u': 3,
    'd': 4, 'm': 4, 'v': 4,
    'e': 5, 'n': 5, 'w': 5,
    'f': 6, 'o': 6, 'x': 6,
    'g': 7, 'p': 7, 'y': 7,
    'h': 8, 'q': 8, 'z': 8,
    'i': 9, 'r': 9
}


def reduce_number(number: int) -> int:
    if number < 10 or number in (11, 22, 33):
        return number
    str_number = str(number)
    split_number = [int(val) for val in str_number.split()]
    result = 0
    for x in split_number:
        result += x
    return reduce_number(result)


def calculate_number(word: str) -> int:
    number = 0
    for letter in word:
        number += letter_number[letter]
    number = reduce_number(number)


def make_numerology(person: Person) -> Person:
    study_data = NumerologyStudyData(person)
