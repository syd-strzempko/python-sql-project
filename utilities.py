import datetime
from extensions import db

def safe_convert(arr):
    return {column.name: safe_convert_single(getattr(arr, column.name)) for column in arr.__table__.columns}

def safe_convert_single(val):
    if isinstance(val, datetime.datetime):
        return val.strftime("%m/%d/%Y, %H:%M:%S")
    if isinstance(val, bool):
        return str(val)
    return val