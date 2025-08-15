from typing import Literal, Optional

from pydantic import BaseModel

from rms.models.v1._enums import DocumentName, FileType


class Evidence(BaseModel):
    value: str
    file_type: Optional[str] = None
    document_name: Optional[DocumentName] = None
    origin_timestamp: Optional[FileType] = None
    version: Literal["1.0.0"] = "1.0.0"
