from datetime import datetime, timedelta

def getNow():
    return datetime.now()+ timedelta(hours=8)

def getDateWithFormat(date, format):
    if date is None or type(date) is datetime:
        return date.strftime(format)
    else: 
        raise RuntimeError('date should be a datetime type variable and non-nullable')


def yesterday():
    return datetime.now()+ timedelta(hours=8) - timedelta(days=1)