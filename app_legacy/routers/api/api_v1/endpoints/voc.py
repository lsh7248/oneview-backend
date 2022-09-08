from typing import List, Tuple

from fastapi import APIRouter, Depends

from app import schemas
from app.db.session import SessionLocal
from app.routers.api.deps import get_db
from app.crud.voc import get_voc_event_by_group_date, get_voc_list_by_group_date, get_voc_trend_by_group_date, get_worst10_bts_by_group_date

router = APIRouter()

# 주기지국 VOC 기준 Worst TOP 10
@router.get("/bts/list", response_model=List[schemas.VocBtsOutput])
async def get_worst_bts(limit: int = 10, team: str = "성남엔지니어링부", start_date: str = "20220510", end_date: str = "20220520", db: SessionLocal = Depends(get_db)):
    worst_bts = get_worst10_bts_by_group_date(db=db, group=team, start_date=start_date, end_date=end_date, limit=limit)
    return worst_bts


@router.get("/list", response_model=List[schemas.VocListOutput])
async def get_vocs_detail(limit: int = 1000, team: str = "성남엔지니어링부", start_date: str = "20220510", end_date: str = "20220520", db: SessionLocal = Depends(get_db)):
    voc_details = get_voc_list_by_group_date(db=db, group=team, start_date=start_date, end_date=end_date, limit=limit)
    return voc_details

@router.get("/trend/day", response_model=List[schemas.VocTrendOutput])
async def get_voc_trend_daily(team: str = "성남엔지니어링부", start_date: str = "20220510", end_date: str = "20220520", db: SessionLocal = Depends(get_db)):
    voc_trend_days = get_voc_trend_by_group_date(db=db, group=team, start_date=start_date, end_date=end_date)
    return voc_trend_days

@router.get("/kpi/day", response_model=schemas.VocEventOutput)
async def get_voc_event_day(team: str = "성남엔지니어링부", date:str="20220502", db: SessionLocal = Depends(get_db)):
    voc_event_day = get_voc_event_by_group_date(db=db, group=team, date=date)
    return voc_event_day















# # 주기지국 Worst TOP 10
# @router.get("/", response_model=List[schemas.JoinVoc])
# async def get_vocs_by_main_bts(limit: int = 10, team: str = None, date: str = None, db: SessionLocal = Depends(get_db)):
#     vocs = get_vocs(db=db, team=team, date=date, limit=limit)
#     return vocs