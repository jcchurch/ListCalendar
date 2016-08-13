#!/usr/bin/env python3

import datetime
import optparse
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

def displaySequentialDates(startStr, endStr, daysOfWeek):
    startDate = createDate(options.startDate)
    endDate = createDate(options.endDate)

    while startDate <= endDate:
        if getLetterCodeForDayOfWeek(startDate) in daysOfWeek:
            print(startDate.strftime("%A. %B %d, %Y"))
        startDate += datetime.timedelta(days=1)

def getLetterCodeForDayOfWeek(date):
    return "MTWRFSU"[ date.weekday() ]

if __name__ == '__main__':
    desc = """List dates in sequential order"""
    p = optparse.OptionParser(usage="%prog [options] [file]", version="%prog 0.1", description=desc)

    p.add_option("-s", "--start", dest="startDate", help="Start Date in YYYY-MM-DD (Required)", metavar="2016-01-01")
    p.add_option("-e", "--end", dest="endDate", help="End Date in YYYY-MM-DD (Required)", metavar="2016-01-31")
    p.add_option("-w", "--dow", dest="daysOfWeek", help="Only print these days of the week: Monday, Tuesday, Wednesday, thuRsday, Friday, Saturday, sUnday. Default is MTWRFSU", metavar="MTWRFSU", default="MTWRFSU")
    options, arguments = p.parse_args()

    if re.match("[MTWRFSUmtwrfsu]+$", options.daysOfWeek) is None:
        raise ValueError("This is not in day of week pattern. Use only the appropriate 1 letter codes.")

    options.daysOfWeek = options.daysOfWeek.upper()

    if options.startDate is not None and options.endDate is not None:
        displaySequentialDates(options.startDate, options.endDate, options.daysOfWeek)
    else:
        print("Both a start date and an end date are required.")
