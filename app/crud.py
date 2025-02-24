from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from .schemas import UFOOrderSchema, OrderResolutionSchema

async def get_ufo_orders(db: AsyncSession, ih_number: str = None, order_id: int = None, customer_order_id: str = None, integration_id: str = None, transaction_id: str = None):
    query = "SELECT * FROM ufo_order_table WHERE 1=1"
    params = {}
    
    if order_id is not None:
        query += " AND order_id = :order_id"
        params["order_id"] = order_id
    if ih_number is not None:
        query += " AND ih_number = :ih_number"
        params["ih_number"] = ih_number
    if customer_order_id is not None:
        query += " AND customer_order_id = :customer_order_id"
        params["customer_order_id"] = customer_order_id
    if integration_id is not None:
        query += " AND integration_id = :integration_id"
        params["integration_id"] = integration_id
    if transaction_id is not None:
        query += " AND transaction_id = :transaction_id"
        params["transaction_id"] = transaction_id
    
    result = await db.execute(text(query), params)
    rows = result.fetchall()

    return [UFOOrderSchema(**row._asdict()) for row in rows]

async def get_order_resolutions(db: AsyncSession, ih_number: str = None, order_id: int = None, customer_order_id: str = None, integration_id: str = None, transaction_id: str = None):
    query = "SELECT * FROM order_resolution WHERE 1=1"
    params = {}
    
    if order_id is not None:
        query += " AND order_id = :order_id"
        params["order_id"] = order_id
    if ih_number is not None:
        query += " AND ih_number = :ih_number"
        params["ih_number"] = ih_number
    if customer_order_id is not None:
        query += " AND customer_order_id = :customer_order_id"
        params["customer_order_id"] = customer_order_id
    if integration_id is not None:
        query += " AND integration_id = :integration_id"
        params["integration_id"] = integration_id
    if transaction_id is not None:
        query += " AND transaction_id = :transaction_id"
        params["transaction_id"] = transaction_id
    
    result = await db.execute(text(query), params)
    rows = result.fetchall()
    return [OrderResolutionSchema(**row._asdict()) for row in rows]