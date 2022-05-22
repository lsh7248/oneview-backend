from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "oracle+cx_oracle://admin:admin@localhost:49161/?service_name=xe&encoding=UTF-8&nencoding=UTF-8"
# cx_Oracle.makedsn("localhost", 49161, sid="xe")
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    # connect_args={
    #     "encoding": "UTF-8",
    #     "nencoding": "UTF-8",
    #     "mode": cx_Oracle.SYSDBA,
    #     "events": True
    # },
    # max_identifier_length=30,
    # connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print("DB Connections Success!")