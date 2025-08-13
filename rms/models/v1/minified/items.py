from dataclasses import dataclass
from typing import Optional


@dataclass
class ItemMin:
    id: str
    foreign_id: str
    description: str
    short_description: Optional[str] = None
    is_controlled: Optional[bool] = None
    category: Optional[str] = None
    subcategory: Optional[str] = None
