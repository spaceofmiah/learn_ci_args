"""
    Simplified approach describing how command line argument
    are implement in python with argparse library.

    
    ===================
    python version: 3.8
    code lesson url:

    Project Description: Project interacts with github's
    API and retrieve a provided number of github zen. It
    can also save the zen's retrieved in a file if stated.
    ===================
"""

import argparse
import requests
import time
from datetime import datetime


# Instantiate ArgumentParser and provide it with program name &
# description. To be shown when --help is called on program module
parser = argparse.ArgumentParser(
    prog="GitZen",
    description="Zen of Git"
)
parser.add_argument(
    "-n", "--num",
    type=int,
    default=1,
    choices=[ value for value in range(1, 6) ],
    help= "Defines the number of zen to retrieve. \
Max of 5 and Min of 1. Defaults to 1 if flag not used in invocation"
)
parser.add_argument(
    "out",
    type=str,
    choices=[ "log", "txt", ],
    help = "Defines where zen would be rendered. (required)"
)

# Retrieve all values supplied to arguments on program
# invocation

args = parser.parse_args()
zens_to_retrieve = args.num
output = args.out

# Create a different file name on every run with datetime lib. &
# replace all spaces on datetime by underscores and colons
# by hyphens. This is so file name can meet supported naming
# format.
date_time_list = datetime.now().strftime("%c").split(" ")
time_list = "_".join(date_time_list).split(":")
file_name = "-".join(time_list)
file_name_and_extension = f"{file_name}.{output}"

# Zen retrieval engine
if output != "log":
    file = open(f"{file_name_and_extension}", "w")
    while zens_to_retrieve > 0:
        time.sleep(20)
        response = requests.get("https://api.github.com/zen")
        file.write(f"> {response.text}\n")
        zens_to_retrieve -= 1
    file.close()
else:
    while zens_to_retrieve > 0:
        time.sleep(20)
        response = requests.get("https://api.github.com/zen")
        print(f"> {response.text}")
        zens_to_retrieve -= 1
    

