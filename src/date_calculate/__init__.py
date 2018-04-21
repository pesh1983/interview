"""Task1.

Implementation of a function that calculates next lottery draw date.
"""
from collections import namedtuple
from datetime import datetime, time, timedelta


def get_next_lottery_date(date=None):
    """Calculate the next Irish lottery draw date.

    :param date: Datetime object is a start date from which the next lottery
    date must be calculated. It is optional, if not defined, the current date
    is taken.
    :return: Datetime object of the next Irish lottery draw date.
    """
    if date is None:
        # if date is not passed
        # get the current one
        date = datetime.now()

    # create class for convenience
    # it stores a day of a week:
    # 0 - Mon, 1 - Tue, 2 - Wed, 3 - Thu, 4 - Fri, 5 - Sat, 6 - Sun
    # and time
    LotteryDay = namedtuple('LotteryDay', ('weekday', 'time'))
    # store weekdays and time when lottery draw takes place
    # this parameter can be passed as a function argument which
    # gives more flexibility
    lottery_days = (
        LotteryDay(weekday=2, time=time(20)),  # Wed, 8pm
        LotteryDay(weekday=5, time=time(20)),  # Sat, 8pm
    )

    # maximum days ahead for the current range
    days_ahead = 7
    # iterate over the current week and the next one
    for week_idx in xrange(2):
        # take each day
        for day in lottery_days:
            # calculate weekday of the current week
            weekday = day.weekday + (week_idx * days_ahead)
            if weekday > date.weekday() or \
                    (weekday == date.weekday() and day.time > date.time()):
                # if weekday of lottery is ahead
                # get only date and throw away time
                date = date.date()
                # add amount of days to the next lottery
                # if current date equals to lottery date then subtraction
                # will give zero
                date += timedelta(days=weekday - date.weekday())
                # combine date and lottery time by that date
                # and return the result
                return datetime.combine(date, day.time)

    # in case something wrong happens return None
    return None
