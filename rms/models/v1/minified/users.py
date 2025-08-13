from dataclasses import dataclass
from typing import Optional


@dataclass
class UserMin:
    id: str
    name: str
    type: Optional[str] = None
    email: Optional[str] = None
