from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class UFOOrderSchema(BaseModel):
    order_id: int
    submitted_date: Optional[datetime]
    reason_code: Optional[str]
    customer_order_id: Optional[str]
    integration_id: Optional[str]
    transaction_id: Optional[str]
    order_status: Optional[str]
    step_status: Optional[str]
    fo_msg: Optional[str]
    src_system: Optional[str]
    ih_number: Optional[str]
    status: Optional[str]
    order_type: Optional[str]

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

class UFOOrderResponse(BaseModel):
    count: int
    data: List[UFOOrderSchema]

class OrderResolutionResponse(BaseModel):
    count: int
    data: List[OrderResolutionSchema]