"""
Utility module
"""

# TODO use date, not datetime because there is no need for time here

import calendar
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
        return move_forward_months(dt, n)
    elif size == "year":
        return move_forward_years(dt, n)


def move_forward_years(dt, nyears):
    new_year = dt.year + nyears
    return fix_day(dt, new_year, dt.month)


def move_forward_months(dt, nmonths):
    year_len = 12
    dyear = nmonths // year_len
    dmonth = nmonths % year_len
    new_year = dt.year + dyear
    new_month = dt.month + dmonth
    return fix_day(dt, new_year, new_month)


def fix_day(old_dt, new_year, new_month):
    """ If the target month is shorter, then set the new day to the last day
    of the month. If the target month is longer, then do not change a day. """
    old_month_len = calendar.monthrange(old_dt.year, old_dt.month)[1]
    new_month_len = calendar.monthrange(new_year, new_month)[1]
    if old_month_len > new_month_len and old_dt.day > new_month_len:
        new_day = new_month_len
    else:
        new_day = old_dt.day
    res = datetime.datetime(new_year, new_month, new_day,
                            old_dt.hour, old_dt.minute, old_dt.second)
    return res


def move_forward_weeks(dt, nweeks):
    return move_forward_days(dt, nweeks * 7)


def move_forward_days(dt, ndays):
    delta = datetime.timedelta(ndays)
    return dt + delta


if __name__ == "__main__":
    pass

