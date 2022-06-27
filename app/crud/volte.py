from sqlalchemy.orm import Session
from sqlalchemy import func, select
from app import schemas

from .. import models


def get_worst_volte_group_by_groups_date(db: Session,
                                      group: str = None,
                                      start_date: str = None,
                                      end_date: str = None,
                                      limit: int = 10):
    pass

def get_worst_volte_bts_by_groups_date(db: Session,
                                      group: str = None,
                                      start_date: str = None,
                                      end_date: str = None,
                                      limit: int = 10):
    pass