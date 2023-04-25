from dataclasses import dataclass
from typing import List


@dataclass
class ProgrammingLanguagesTableRaw:
    website_name: str
    popularity: int
    frontend: str
    backend: str


@dataclass
class ProgrammingLanguagesTable:
    rows: List[ProgrammingLanguagesTableRaw]
    index = 0

