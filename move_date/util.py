"""
Utility module
"""

import calendar
import datetime


def date2():
    return 'stub2'


def move_backward(dt, step):
    (n, size) = step
    if size == "day":
        return move_backward_days(dt, n)
    elif size == "week":
        return move_backward_weeks(dt, n)
    elif size == "month":
        return move_backward_months(dt, n)
    elif size == "year":
        return move_backward_years(dt, n)


def move_backward_days(dt, ndays):
    delta = datetime.timedelta(ndays)
    return dt - delta


def move_backward_weeks(dt, nweeks):
    return move_backward_days(dt, nweeks * 7)


def move_backward_months(dt, nmonths):
    new_month = dt.month - nmonths
    if new_month < 1:
        year_len = 12
        m2 = new_month
        m3 = year_len - (-m2 % year_len)
        dy = -m2 // year_len + 1
        print("m back m: {} {} {}".format(m2, m3, dy))
        return fix_date(dt, dt.year - dy, m3)
    else:
        return fix_date(dt, dt.year, new_month)


def move_backward_years(dt, ndays):
    pass


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
    return fix_date(dt, new_year, dt.month)


def move_forward_months(dt, nmonths):
    new_month = dt.month + nmonths
    if new_month > 12:
        year_len = 12
        dyear = new_month // year_len
        month = new_month % year_len
        y2 = dt.year + dyear
        m2 = month
        return fix_day(dt, y2, m2)
    else:
        return fix_day(dt, dt.year, new_month)


def fix_date(dt, new_year, new_month):
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
    res = datetime.date(new_year, new_month, new_day)
    return res


def move_forward_weeks(dt, nweeks):
    return move_forward_days(dt, nweeks * 7)


def move_forward_days(dt, ndays):
    delta = datetime.timedelta(ndays)
    return dt + delta


if __name__ == "__main__":
    pass

