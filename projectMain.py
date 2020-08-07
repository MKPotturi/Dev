import math
import os
import sys

import requests

 version_details = "Python Version ==  " + sys.version
 path_details = "PATH for Python == " + sys.executable


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting

"""
Given the year and you have to write a function to check if the year is leap or not. In the Gregorian calendar three criteria must be taken into account to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
"""

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)

def printo():
    print(greet("Murali"))
    print("*******************")
    print(version_details)
    print("*******************")
    print(path_details)
    r = requests.get("https://www.linkedin.com/in/mpotturi/")
    print(r.status_code)


def main():
    printo()


if __name__ == "__main__":
    main()
