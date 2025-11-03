from typing import Any, List, Optional

from pydantic import BaseModel
import os

MODE = os.getenv("APP_MODE", "TESTING")  # or MODE = "DEPLOYMENT"

if MODE == "DEPLOYMENT":
    from diag_app.apps_interface.data.faults.types import Fault
if MODE == "TESTING":
    from apps_interface.data.faults.types import Fault

class ListOfFaults(BaseModel):
    '''Retrieve list of all faults provided by the entity'''
    items: List[Fault]
    schema: Optional[Any] = None