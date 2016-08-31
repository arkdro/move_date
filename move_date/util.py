"""
Utility module
"""


import datetime


def date2():
    return 'stub2'


def move_forward(dt, step):
    (n, size) = step
    if size == "day":
        return move_forward_days(dt, n)
    elif size == "week":
        return move_forward_weeks(dt, n)
    elif size == "month":
        pass
    elif size == "year":
        pass


def move_forward_weeks(dt, nweeks):
    return move_forward_days(dt, nweeks * 7)


def move_forward_days(dt, ndays):
    delta = datetime.timedelta(ndays)
    return dt + delta


if __name__ == "__main__":
    pass

