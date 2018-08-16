"""

# Create User and Database

    CREATE USER 'cabin'@'localhost' IDENTIFIED BY 'cabin';
    GRANT ALL PRIVILEGES ON *.* TO 'cabin'@'localhost';
    CREATE DATABASE cabin;

"""


import argparse
import json
import os

from calendarcabin.database import get_url, get_session, create_all_tables
from calendarcabin.models.calendar import Calendar 
from calendarcabin.models.event import Event


cdir = os.path.abspath(os.path.dirname(__file__))


def read_events(path, calendar_id):
    with open(path) as f:
        data = json.load(f)

        for obj in data:
            event = Event(
                title=obj.get('title'),
                start=obj.get('start'),
                end=obj.get('end'),
                url=obj.get('url'),
                repeat_id=obj.get('id'),
                calendar_id=calendar_id,
                )
            yield event


def run(options):
    url = get_url(username=options.username, password=options.password, host=options.host, dbname=options.dbname)
    session, engine = get_session(url)
    create_all_tables(engine)

    def commit():
        session.flush()
        session.commit()

    # Create Calendar
    calendar = Calendar()
    session.add(calendar)
    commit()

    # Create Events
    for i, event in enumerate(read_events(options.events, calendar.id)):
        session.add(event)

        if i % 100 == 0:
            commit()
    commit()

    print('calendar.id = {}'.format(calendar.id))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--events', type=str, default=os.path.join(cdir, '..', 'example', 'events.json'))

    # DB Parameters
    parser.add_argument('--username', type=str, default='cabin')
    parser.add_argument('--password', type=str, default='cabin')
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--dbname', type=str, default='cabin')

    options = parser.parse_args()

    print(json.dumps(options.__dict__, sort_keys=True, indent=4))

    run(options)
