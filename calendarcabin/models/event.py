from sqlalchemy import Column, Integer, String

from calendarcabin.models import Base


class Event(Base):
    __tablename__ = 'event'
    
    id = Column(Integer(), primary_key=True)
    repeat_id = Column(Integer()) 
    title = Column(String(256))
    url = Column(String(256))
    start = Column(String(256))
    end = Column(String(256))

    # Foreign Key
    calendar_id = Column(Integer())
