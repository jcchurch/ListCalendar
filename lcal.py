#!/usr/bin/env python3

import datetime
import optparse
import re

def createDate(stringDate):
    if re.match("\d\d\d\d-\d\d-\d\d", stringDate) is None:
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

def displaySequentialDates(startStr, endStr):
    startDate = createDate(options.startDate)
    endDate = createDate(options.endDate)

    while startDate <= endDate:
        print(startDate.strftime("%A. %B %d, %Y"))
        startDate += datetime.timedelta(days=1)

if __name__ == '__main__':
    desc = """List dates in sequential order"""
    p = optparse.OptionParser(usage="%prog [options] [file]", version="%prog 0.1", description=desc)

    p.add_option("-s", "--start", dest="startDate", help="Start Date in YYYY-MM-DD", metavar="2016-01-01")
    p.add_option("-e", "--end", dest="endDate", help="End Date in YYYY-MM-DD", metavar="2016-01-31")
    options, arguments = p.parse_args()

    if options.startDate is not None and options.endDate is not None:
        displaySequentialDates(options.startDate, options.endDate)
