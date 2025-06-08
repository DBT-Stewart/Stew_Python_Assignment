import calendar

def get_day_name(month, day, year):
    """
    Returns the name of the day for a given date in uppercase.
    """
    day_index = calendar.weekday(year, month, day)
    return calendar.day_name[day_index].upper()