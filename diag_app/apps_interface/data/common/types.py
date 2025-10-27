from enum import Enum
from typing import Any, List, Optional
import os
from pydantic import BaseModel

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.common.errors import DataError
if MODE == "TESTING":
    from apps_interface.data.common.errors import DataError

class ValueMetaData(BaseModel):
    """Description of a value""" 
    id: str
    name: str
    translation_id: Optional[str] = None
    category: str                               
    groups: Optional[List[str]] = None

class ReadValue(BaseModel):
    """Single data value"""

    id: str
    data: Any
    errors: Optional[List[DataError]] = None

