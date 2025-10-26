from typing import Any, Optional

from pydantic import BaseModel

class GenericError(BaseModel):
    """It is recommended that the response body of an error response includes a more detailed description of the error which helps in diagnosing the issue."""

    error_code: str
    vendor_code: Optional[str] = None
    message: str
    translation_id: Optional[str] = None
    parameters: Optional[Any] = None

class DataError(BaseModel):
    """On some occasions an error applies only to parts of a response, e.g.,
    when reading a data resource. In this case the type DataError is used
    which includes a path to the erroneous attribute of the response."""

    path: str
    error: Optional[GenericError]