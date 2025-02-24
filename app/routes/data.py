
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from ..db import get_db
from ..crud import get_ufo_orders, get_order_resolutions
from ..schemas import UFOOrderResponse, OrderResolutionResponse
from typing import List

router = APIRouter()

@router.get("/ufo_orders", response_model=UFOOrderResponse)
async def fetch_ufo_orders(
    ih_number: str = Query(None, description="Filter by IH Number"),
    order_id: int = Query(None, description="Filter by Order ID"),
    customer_order_id: str = Query(None, description="Filter by Customer Order ID"),
    integration_id: str = Query(None, description="Filter by Integration ID"),
    transaction_id: str = Query(None, description="Filter by Transaction ID"),
    db: AsyncSession = Depends(get_db)
):
    responseList = await get_ufo_orders(db, ih_number, order_id, customer_order_id, integration_id, transaction_id)
    return UFOOrderResponse(count=len(responseList), data=responseList)

@router.get("/order_resolutions", response_model=OrderResolutionResponse)
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