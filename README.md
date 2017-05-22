# ListCalendar

## Overview

ListCalendar is a command line tool which displays all of the dates for a supplied range in a human readable format.

## Required software

ListCalendar requires Python 3.

## Usage

To use ListCalendar, use the following options:

    -h, --help            show this help message and exit
    -s 2016-01-01, --start 2016-01-01
                          Start Date in YYYY-MM-DD. Uses current date as the default.
    -e 2016-01-31, --end 2016-01-31
                          End Date in YYYY-MM-DD (Required)
    -d MTWRFSU, --dow MTWRFSU
                          Only print these days of the week: Monday, Tuesday,
                          Wednesday, thuRsday, Friday, Saturday, sUnday. Default
                          is MTWRFSU
    -f '%Y-%m-%d', --format '%Y-%m-%d'
                          Specify Date Format. Uses Python3's datetime format.
                          Default is '%A. %B %d, %Y'

## Examples

Print all of the dates from January 1, 2016 to January 30, 2016, but only those that land on Monday, Wednesday, or Friday.

    $ ./lcal.py -s 2016-01-01 -e 2016-01-30 -d MWF
    Friday. January 01, 2016
    Monday. January 04, 2016
    Wednesday. January 06, 2016
    Friday. January 08, 2016
    Monday. January 11, 2016
    Wednesday. January 13, 2016
    Friday. January 15, 2016
    Monday. January 18, 2016
    Wednesday. January 20, 2016
    Friday. January 22, 2016
    Monday. January 25, 2016
    Wednesday. January 27, 2016
    Friday. January 29, 2016
