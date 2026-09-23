from dataclasses import dataclass, asdict
from typing import List, Optional

@dataclass
class Recipe:
    name: str
    ingredients: List[str]
    steps: List[str]
    cuisine: str
    prep_time: str
    difficulty: Optional[str] = None
    servings: Optional[int] = None

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data.get('name', 'Unknown'),
            ingredients=data.get('ingredients', []),
            steps=data.get('steps', []),
            cuisine=data.get('cuisine', 'Unknown'),
            prep_time=data.get('prep_time', 'Unknown'),
            difficulty=data.get('difficulty'),
            servings=data.get('servings')
        )
