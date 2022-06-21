from typing import List, Tuple

from fastapi import APIRouter, Depends

from app import schemas
from app.db.session import SessionLocal
from app.routers.api.deps import get_db
from app.crud.voc import get_vocs

router = APIRouter()

# VOC 전체목록 선택조회 api
@router.get("/list/", response_model=List[schemas.JoinVoc])
async def get_vocs_all(
    start_date: str,
    end_date: str,
    select_by: str,
    belong_name: str,
    limit: int=100,
    db: SessionLocal = Depends(get_db)):
    pass

# 주기지국 Worst TOP 10
@router.get("/", response_model=List[schemas.JoinVoc])
async def get_vocs_by_main_bts(limit: int = 10, team: str = None, date: str = None, db: SessionLocal = Depends(get_db)):
    vocs = get_vocs(db=db, team=team, date=date, limit=limit)
    return vocs