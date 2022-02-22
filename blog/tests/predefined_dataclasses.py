from dataclasses import dataclass
from datetime import date

@dataclass
class PostDataClass:
    title      : str
    subtitle   : str
    body       : str
    created_at : date
    updated_at : date

@dataclass
class TagDataClass:
    name       : str
