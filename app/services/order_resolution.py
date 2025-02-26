from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.schemas import OrderResolutionSchema

async def get_order_resolutions_lov(db: AsyncSession, error_code: str = None):
    query = "SELECT * FROM order_resolution_lookup WHERE 1=1"
    params = {}
    
    if error_code is not None:
        query += " AND error_code = :error_code"
        params["error_code"] = error_code
    
    result = await db.execute(text(query), params)
    rows = result.fetchall()
    return [OrderResolutionSchema(**row._asdict()) for row in rows]

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

async def insert_order_resolution(db: AsyncSession, resolution: OrderResolutionSchema):
    query = text("""
        INSERT INTO order_resolution_table (action_timestamp, order_id, submitted_date, integration_id, 
                                            transaction_id, ih_number, system, root_cause_analysis, action_taken, costumer_order_id) 
        VALUES (:action_timestamp, :order_id, :submitted_date, :integration_id, 
                :transaction_id, :ih_number, :system, :root_cause_analysis, :action_taken, :costumer_order_id)
        RETURNING *
    """)
    result = await db.execute(query, resolution.dict())
    await db.commit()
    return result.fetchone()

async def update_order_resolution(db: AsyncSession, order_id: int, ih_number: str, resolution_update: dict):
    set_clause = ", ".join([f"{key} = :{key}" for key in resolution_update.keys()])
    query = text(f"""
        UPDATE order_resolution_table
        SET {set_clause}
        WHERE order_id = :order_id AND ih_number = :ih_number
        RETURNING *
    """)
    params = {"order_id": order_id, "ih_number": ih_number, **resolution_update}
    result = await db.execute(query, params)
    await db.commit()
    return result.fetchone()