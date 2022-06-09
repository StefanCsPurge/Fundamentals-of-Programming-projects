"""

2. Compute the age of a person in number of days. So, given the date of birth
of a person in the format dd mm yyyy (three integers) and the current date
(in the same format) compute the age of that person in number of days.

"""


def is_leap(y):
    if y % 400 == 0:
        return True
    return y % 4 == 0 and y % 100 != 0


def days_of_month(m):
    if m in (4, 6, 9, 11):
        return 30
    return 31


def number_of_days(d, m, y):
    """Computes the number of days that have passed from the beginning of the year
    y until the date given in the arguments"""
    days = d
    
    for month in range(1, m):
        if month == 2:
            if is_leap(y):
                days +=29
            else:
                days += 28
        else:
            days += days_of_month(month)
        #print(days, end=' ')
    return days


def compute_age(d1, m1, y1, d2, m2, y2):
    age = number_of_days(d2, m2, y2)
    for year in range(y1, y2):
        age += 365
        if is_leap(year):
            age += 1
    return age - number_of_days(d1, m1, y1)


if __name__ == '__main__':
    d1, m1, y1 = 24, 1, 2015
    d2, m2, y2 = 5, 10, 2018
    print("Age in number of days of (d1={0}, m1={1}, y1={2}, d2={3}, m2={4}, y2={5}, )"
          " is: {6}".format(d1, m1, y1, d2, m2, y2, compute_age(d1, m1, y1, d2, m2, y2)))
    #print(number_of_days(5, 10, 2018))
    
