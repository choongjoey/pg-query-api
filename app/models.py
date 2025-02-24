from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UFOOrderTable(Base):
    __tablename__ = "ufo_order_table"
    order_id = Column(Integer, primary_key=True, index=True)
    submitted_date = Column(TIMESTAMP, nullable=True)
    reason_code = Column(String(10), nullable=True)
    customer_order_id = Column(String(25), nullable=True)
    integration_id = Column(String(25), nullable=True)
    transaction_id = Column(String(43), nullable=True)
    order_status = Column(String(15), nullable=True)
    step_status = Column(String(15), nullable=True)
    fo_msg = Column(String(40), nullable=True)
    src_system = Column(String(40), nullable=True)
    ih_number = Column(String(16), nullable=True)
    status = Column(String(15), nullable=True)
    order_type = Column(String(5), nullable=True)

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