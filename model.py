# coding: utf-8

from sqlalchemy import create_engine, types, Column, Integer, String, DateTime, Boolean, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime
from config import DB_STRING

engine = create_engine(DB_STRING, echo=True, pool_recycle=3600)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True)
    todo = Column(String(255))
    created_at = Column(TIMESTAMP, default=datetime.now)
