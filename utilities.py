import datetime

def safe_convert(val):
    if isinstance(val, datetime.datetime):
        return val.strftime("%m/%d/%Y, %H:%M:%S")
    if isinstance(val, bool):
        return str(val)
    return val