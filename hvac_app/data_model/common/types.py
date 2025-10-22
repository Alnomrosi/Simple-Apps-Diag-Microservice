from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel

class ValueMetaData(BaseModel):
    """Description of a value""" 
    id: str
    name: str
    translation_id: Optional[str] = None
    category: str                               
    groups: Optional[List[str]] = None

