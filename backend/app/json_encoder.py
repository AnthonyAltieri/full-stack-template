from datetime import date, datetime

from flask.json import JSONEncoder


class JSONEncoderWithDateLikeSupport(JSONEncoder):
    """
    Adds JSON encoding for datetime.date and datetime.datetime as a string in isoformat

    """

    def default(self, o):
        if isinstance(o, date):
            return datetime(day=o.day, month=o.month, year=o.year).isoformat()
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)
