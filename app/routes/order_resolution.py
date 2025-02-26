from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db
from app.services.order_resolution import insert_order_resolution, update_order_resolution, get_order_resolutions
from app.schemas import OrderResolutionResponse, OrderResolutionSchema

router = APIRouter(prefix="/order_resolution", tags=["Order Resolution"])

@router.post("/")
async def create_order_resolution(resolution: OrderResolutionSchema, db: AsyncSession = Depends(get_db)):
    return await insert_order_resolution(db, resolution)

@router.put("/{order_id}")
async def modify_order_resolution(order_id: int, resolution: OrderResolutionSchema, db: AsyncSession = Depends(get_db)):
    return await update_order_resolution(db, order_id, resolution)

@router.get("/", response_model=OrderResolutionResponse)
async def fetch_order_resolutions(
    ih_number: str = Query(None, description="Filter by IH Number"),
    order_id: int = Query(None, description="Filter by Order ID"),
    customer_order_id: str = Query(None, description="Filter by Customer Order ID"),
    integration_id: str = Query(None, description="Filter by Integration ID"),
    transaction_id: str = Query(None, description="Filter by Transaction ID"),
    db: AsyncSession = Depends(get_db)
):
    responseList = await get_order_resolutions(db, ih_number, order_id, customer_order_id, integration_id, transaction_id)
    return OrderResolutionResponse(count=len(responseList), data=responseList)