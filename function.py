from datetime import datetime,timezone
def timediff_custom(date_given,type_flag=['s']):
    """
    A function that calculates difference between two dates
    and returns the absolute difference in seconds/minutes
    /hours/days 
    """
    a = date_given
    b = datetime.now(timezone.utc)
    c = b - a
    if c.seconds >= 60:
        type_flag.pop(0)
        type_flag.append('m')
        return int(c.seconds/60)
    elif c.seconds >=3600:
        type_flag.pop(0)
        type_flag.append('h')
        return int(c.seconds/3600)
    elif c.seconds >= 86400:
        type_flag.pop(0)
        type_flag.append('d')
        return int(c.seconds/86400)
    return c.seconds
