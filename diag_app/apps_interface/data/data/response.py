from typing import Any, List, Optional
import os
from pydantic import BaseModel

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.common.types import ValueMetaData, ReadValue
if MODE == "TESTING":
    from apps_interface.data.common.types import ValueMetaData, ReadValue


class Datas(BaseModel):
    """Response: Retrieve list of all data provided by the entity"""

    items: List[ValueMetaData] = []
    #schema: Optional[Any] = None



class DataValue(ReadValue):
    """Response: Read single data value from an entity"""
    id: str
    data: Any
    #schema: Optional[Any] = None