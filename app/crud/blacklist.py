from sqlalchemy.orm import Session

from .. import models, schemas

def create_blacklist(db: Session, token: schemas.TokenCreate, user_id: int):
    db_item = models.Item(**token.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
