def leap_year(year):
    """:param year: int - year given as an arg
        :return: int - if is a leap year or not """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False
