import argparse

from calendarcabin.server.app import launch
from calendarcabin.database import get_url


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # DB Parameters
    parser.add_argument('--username', type=str, default='cabin')
    parser.add_argument('--password', type=str, default='cabin')
    parser.add_argument('--host', type=str, default='localhost')
    parser.add_argument('--dbname', type=str, default='cabin')

    options = parser.parse_args()

    url = get_url(username=options.username, password=options.password, host=options.host, dbname=options.dbname)

    launch(url=url)
