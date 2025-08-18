from dataclasses import dataclass
from typing import Literal, Optional

from rms.models.v1._enums import DocumentName, FileType


@dataclass
class Evidence:
    value: str
    file_type: Optional[str] = None
    document_name: Optional[DocumentName] = None
    origin_timestamp: Optional[FileType] = None
    version: Literal["1.0.0"] = "1.0.0"
