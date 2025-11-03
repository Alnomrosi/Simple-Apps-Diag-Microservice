from typing import Any, List, Optional

from pydantic import BaseModel, Field

class FaultStatus(BaseModel):
    aggregatedStatus: str

class Fault(BaseModel):
    '''Fault code in the native representation of the entity.'''
    code: str
    scope: Optional[str] = None
    display_code: Optional[str]
    fault_name: str
    fault_translation_id: Optional[str] = None
    severity: Optional[str]  = None
    status: Optional[FaultStatus]
    symptom: Optional[str] = None
    symptom_transaction_id: Optional[str] = None