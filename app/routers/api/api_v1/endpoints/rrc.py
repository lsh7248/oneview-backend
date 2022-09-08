from typing import List, Tuple

from fastapi import APIRouter, Depends

from app import schemas
from app.db.session import SessionLocal
from app.routers.api.deps import get_db
from app.crud.rrc import get_rrc_trend_by_group_date, get_worst10_rrc_bts_by_group_date


router = APIRouter()


@router.get("/trend-day", response_model=List[schemas.RrcTrendOutput])
async def get_rrc_trend_day(group:str="", start_date: str = "20220810", end_date: str = None, db: SessionLocal = Depends(get_db)):
    rrc_trend_days = get_rrc_trend_by_group_date(db=db, group=group, start_date=start_date, end_date=end_date)
    return rrc_trend_days


@router.get("/worst", response_model=List[schemas.RrcBtsOutput])
async def get_worst_rrc_bts(limit: int = 10, group:str="", start_date: str = "20220801", end_date: str = None, db: SessionLocal = Depends(get_db)):
    worst_rrc_bts = get_worst10_rrc_bts_by_group_date(db=db, group=group, start_date=start_date, end_date=end_date, limit=limit)
    return worst_rrc_bts