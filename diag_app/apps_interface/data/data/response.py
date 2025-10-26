from typing import Any, List, Optional
import os
from pydantic import BaseModel

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.common.types import ValueMetaData
if MODE == "TESTING":
    from apps_interface.data.common.types import ValueMetaData


class Datas(BaseModel):
    """Response: Retrieve list of all data provided by the entity"""

    items: List[ValueMetaData] = []
    schema: Optional[Any] = None