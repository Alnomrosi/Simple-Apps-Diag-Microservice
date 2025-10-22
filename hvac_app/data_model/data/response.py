from typing import Any, List, Optional
import os
from pydantic import BaseModel

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from hvac_app.data_model.common.types import ValueMetaData
if MODE == "TESTING":
    from data_model.common.types import ValueMetaData


class Datas(BaseModel):
    """Response: Retrieve list of all data provided by the entity"""

    items: List[ValueMetaData] = []
    schema: Optional[Any] = None