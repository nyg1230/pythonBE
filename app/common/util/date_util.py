from datetime import datetime, timedelta
from enum import Enum
import math

class DateEnum(Enum):
    w = "week"
    d = "days"
    h = "hours"
    m = "minutes"
    s = "seconds"
    ms = "milliseconds"

def get_now_timestamp():
    return math.floor(datetime.utcnow().timestamp())

def add_datetime_unit(t_datetime: datetime, add_value = 0, unit = "ms"):
    kwargs = dict()
    t_unit = None
    if (unit in DateEnum._member_map_):
        t_unit = DateEnum.__getitem__(unit).value
    else:
        t_unit = DateEnum.ms.value
    kwargs.setdefault(t_unit, add_value)
    delta = timedelta(**kwargs)
    result = t_datetime + delta

    return result

def timestamp_2_datetime(timestamp, GMT = 0):
    result = datetime.fromtimestamp(timestamp)
    return add_datetime_unit(result, GMT, "h")
