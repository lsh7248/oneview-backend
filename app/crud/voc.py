from sqlalchemy.orm import Session
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