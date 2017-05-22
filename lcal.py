#!/usr/bin/env python3

import datetime
import argparse
import re

def createDate(stringDate):
    if re.match("\d\d\d\d-\d\d-\d\d$", stringDate) is None:
        raise ValueError("This is not in the correct date format. Use YYYY-MM-DD")

    (yearStr, monthStr, dayStr) = stringDate.split("-")
    year = int(yearStr)
    month = int(monthStr)
    day = int(dayStr)

    if year < 1970:
        raise ValueError("Year is less than 1970.")

    if year > 2100:
        raise ValueError("Year is greater than 2100.")

    if month < 1 or month > 12:
        raise ValueError("Month is not 01 to 12.")

    if day < 1 or day > 31:
        raise ValueError("Day is not 01 to 31.")

    return datetime.date(year, month, day)

def displaySequentialDates(startStr, endStr, daysOfWeek, dateFormat):
    startDate = createDate(options.startDate)
    endDate = createDate(options.endDate)

    while startDate <= endDate:
        if getLetterCodeForDayOfWeek(startDate) in daysOfWeek:
            print(startDate.strftime(dateFormat))
        startDate += datetime.timedelta(days=1)

def getLetterCodeForDayOfWeek(date):
    return "MTWRFSU"[ date.weekday() ]

if __name__ == '__main__':
    p = argparse.ArgumentParser(description="List dates in sequential order")

    p.add_argument("-s", "--start", metavar="2016-01-01", dest="startDate",
                   help="Start Date in YYYY-MM-DD (Required)")
    p.add_argument("-e", "--end", dest="endDate",
                   help="End Date in YYYY-MM-DD (Required)", metavar="2016-01-31")
    p.add_argument("-d", "--dow", dest="daysOfWeek", metavar="MTWRFSU", default="MTWRFSU",
                   help="Only print these days of the week: Monday, Tuesday, Wednesday, thuRsday, Friday, Saturday, sUnday. Default is MTWRFSU")
    p.add_argument("-f", "--format", dest="dateFormat", metavar="'%Y-%m-%d'", default="%A. %B %d, %Y",
                   help="Specify Date Format. Uses Python3's datetime format. Default is '%%A. %%B %%d, %%Y'")
    options = p.parse_args()

    if re.match("[MTWRFSUmtwrfsu]+$", options.daysOfWeek) is None:
        raise ValueError("This is not in day of week pattern. Use only the appropriate 1 letter codes.")

    options.daysOfWeek = options.daysOfWeek.upper()

    if options.startDate is not None and options.endDate is not None:
        displaySequentialDates(options.startDate, options.endDate, options.daysOfWeek, options.dateFormat)
    else:
        print("Both a start date and an end date are required.")
