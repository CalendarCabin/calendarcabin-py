from sqlalchemy import Column, Integer, String

from calendarcabin.models import Base


class Calendar(Base):
    __tablename__ = 'calendar'
    
    id = Column(Integer(), primary_key=True)
