from dataclasses import dataclass

@dataclass
class PostDataClass:
    title      : str
    subtitle   : str
    body       : str
    created_at : date
    updated_at : date
