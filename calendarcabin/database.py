from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from calendarcabin.models import Base
from calendarcabin.models.calendar import Calendar
from calendarcabin.models.event import Event


def get_url(username='cabin', password='cabin', host='localhost', dbname='cabin'):
    url = "mysql+pymysql://{username}:{password}@{host}/{dbname}".format(
        username=username,
        password=password,
        host=host,
        dbname=dbname)

    return url


def get_session(url):
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session, engine


def create_all_tables(engine):
    Base.metadata.create_all(engine)


class DB(object):
    def __init__(self, url):
        self.url = url
        self.session, _ = get_session(url)

    def get_calendars(self):
        return self.session.query(Calendar).all()

    def get_calendar_events(self, calendar_id):
        return self.session.query(Event).filter(Event.calendar_id == calendar_id).all()
