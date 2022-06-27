from sqlalchemy.orm import Session
from sqlalchemy import func, select, case
from app import schemas

from .. import models

def get_vocs(db: Session, team: str = None, date: str = None, limit: int = 10):

    _vocs = db.query(models.Voc, models.Bts).join(models.Bts, models.Voc.sbt_bts_cd == models.Bts.sbt_bts_cd, isouter=True)
    if date:
        _vocs = _vocs.filter(models.Voc.base_date == date)
    if team:
        _vocs = _vocs.filter(models.Bts.oper_team_nm == team)
    _vocs = _vocs.order_by(models.Voc.sr_tt_rcp_no.desc()).limit(50).all()

    list_vocs = list(map(lambda models: schemas.JoinVoc(
                # base_ym = models[0].base_ym,
                voc_wjt_qrtc_nm = models[0].voc_wjt_qrtc_nm,
                equip_cd = models[0].equip_cd,
                sr_tt_rcp_no = models[0].sr_tt_rcp_no,
                base_date = models[0].base_date,
                sbt_bts_cd = models[0].sbt_bts_cd,

                equip_nm = models[1].equip_nm,
                cell_cd = models[1].cell_cd,
                oper_team_nm = models[1].oper_team_nm,
                addr_dtl = models[1].addr_dtl,
                bld_flor = models[1].bld_flor,
                biz_hq_nm = models[1].biz_hq_nm
                ), _vocs))

    return list_vocs[:limit]


def get_most_voc_bts_by_group_date(db: Session, jo: str = None, start_date: str = None, end_date: str = None, limit: int = 10):
    entities_worst10 = [
        models.Voc.base_ym,
        models.Voc.base_date,
        models.Voc.equip_cd0,
        models.Voc.sido_nm,
        models.Voc.eup_myun_dong_nm,
        models.Voc.bts_oper_team_nm,
        models.Voc.adm_cd1,
        models.Voc.wjxbfs1
    ]
    func.sum(case(value=models.Voc.wjxbfs1, whens={3: 1}, else_=0)).label("voc_cnt")

    pass

def get_voc_count_group_by_group_date(db: Session, jo: str = None, start_date: str = None, end_date: str = None, limit: int = 10):
    entities_worst10 = [
        models.Voc.base_ym,
        models.Voc.base_date,
        models.Voc.equip_cd0,
        models.Voc.sido_nm,
        models.Voc.eup_myun_dong_nm,
        models.Voc.bts_oper_team_nm,
        models.Voc.adm_cd1,
    ]
    sum_fn = func.count(models.Voc.wjxbfs1).label("voc_cnt")
    pass

def get_voc_count_group_by_group_month(db: Session, jo: str = None, start_date: str = None, end_date: str = None, limit: int = 10):
    entities_worst10 = [
        models.Voc.base_ym,
        models.Voc.base_date,
        models.Voc.equip_cd0,
        models.Voc.sido_nm,
        models.Voc.eup_myun_dong_nm,
        models.Voc.bts_oper_team_nm,
        models.Voc.adm_cd1,
    ]
    sum_fn = func.count(models.Voc.wjxbfs1).label("voc_cnt")
    pass