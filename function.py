from datetime import datetime,timezone
from math import floor
def timediff_custom(date_given,type_flag=['s'],plural=[False]):
    """
    A function used to check difference between modified/updated and current time
    a handy function for use in apps.
    """
    a = date_given
    b = datetime.now(timezone.utc)
    c = b - a
    timeToCheck= int(floor(c.total_seconds()))
    if timeToCheck >= 60 and timeToCheck < 3600:
        type_flag.pop(0)
        type_flag.append('m')
        newTimeToCheck = int(floor(timeToCheck/60))
        if newTimeToCheck > 1:
            plural.pop(0)
            plural.append(True)
        return newTimeToCheck 
    elif timeToCheck >=3600 and timeToCheck < 86400:
        type_flag.pop(0)
        type_flag.append('h')
        newTimeToCheck =int(floor(timeToCheck/3600))
        if newTimeToCheck > 1:
            plural.pop(0)
            plural.append(True)
        return newTimeToCheck
    elif timeToCheck >= 86400:
        type_flag.pop(0)
        type_flag.append('d')
        newTimeToCheck =int(floor(timeToCheck/86400))
        if newTimeToCheck > 1:
            plural.pop(0)
            plural.append(True)
        return newTimeToCheck
    if timeToCheck>1:
        plural.pop(0)
        plural.append(True)
    return int(floor(timeToCheck))
