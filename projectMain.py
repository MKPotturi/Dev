import math
import os
import sys

import requests

version_details = "Python Version ==  " + sys.version
path_details = "PATH for Python == " + sys.executable


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


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
