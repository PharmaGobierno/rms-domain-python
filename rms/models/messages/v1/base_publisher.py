from dataclasses import asdict, dataclass, field
from time import time
from typing import Any, Dict, Optional

from rms.models.v1.minified.users import UserMin


@dataclass
class BasePubsubMessage:
    payload: Any
    origin_timestamp: int
    author: UserMin
    version: str
    published_at: int = field(default_factory=lambda: round(time() * 1000))
    context: Optional[dict] = None

    def dict(self):
        return asdict(self)

    @classmethod
    def topic(cls) -> str:
        raise NotImplementedError

    def get_attributes(self) -> Dict[str, str]:
        return {"topic": self.topic(), "version": self.version}


@dataclass
class BaseKafkaMessage:
    payload: Any
    origin_timestamp: int
    author: UserMin
    version: str
    published_at: int = field(default_factory=lambda: round(time() * 1000))
    context: Optional[dict] = None

    def dict(self):
        return asdict(self)

    def topic(self) -> str:
        raise NotImplementedError

    def get_headers(self) -> Dict[str, str]:
        return {"topic": self.topic(), "version": self.version}
