from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderResolutionSchema(BaseModel):
    order_id: int
    action_timestamp: Optional[datetime]
    submitted_date: Optional[datetime]
    integration_id: Optional[str]
    transaction_id: Optional[str]
    ih_number: str
    system: Optional[str]
    root_cause_analysis: Optional[str]
    action_taken: Optional[str]
    customer_order_id: Optional[str]

class OrderResolutionResponse(BaseModel):
    count: int
    data: List[OrderResolutionSchema]