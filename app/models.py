from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OrderResolution(Base):
    __tablename__ = "order_resolution"
    action_timestamp = Column(TIMESTAMP, nullable=True)
    order_id = Column(Integer, primary_key=True, index=True)
    submitted_date = Column(TIMESTAMP, nullable=True)
    integration_id = Column(String(25), nullable=True)
    transaction_id = Column(String(43), nullable=True)
    ih_number = Column(String(16), nullable=False)
    system = Column(String(40), nullable=True)
    root_cause_analysis = Column(String(255), nullable=True)
    action_taken = Column(String(255), nullable=True)
    customer_order_id = Column(String(25), nullable=True)

class OrderResolutionLookup(Base):
    __tablename__ = "order_resolution_lookup"
    id = Column(Integer, primary_key=True, index=True)
    error_code = Column(String(40), nullable=True)
    error_description = Column(String(255), nullable=True)
    error_category = Column(String(40), nullable=True)
    error_group = Column(String(40), nullable=True)
    transaction_type = Column(String(40), nullable=True)
    root_cause = Column(String(255), nullable=True)
    next_action = Column(String(255), nullable=True)
    pic = Column(String(40), nullable=True)
    contact_person = Column(String(40), nullable=True)