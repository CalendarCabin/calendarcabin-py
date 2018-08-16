from json import JSONEncoder

from sqlalchemy import inspect

from calendarcabin.models import Base


def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}


class SQLAlchemyJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, Base):
                return object_as_dict(obj)
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)
