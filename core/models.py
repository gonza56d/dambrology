from pydantic import BaseModel as PydanticModel


class Numerology(PydanticModel):

    essence: int
    image: int
    destiny: int
    path: int


class Person(PydanticModel):

    first_name: str
    last_name: str
    numerology: Numerology | None = None
