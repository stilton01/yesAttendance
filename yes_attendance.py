# Autofill Google Form

import requests
import datetime
import time
import sys

# URL to the form you want to fill. formResponse should be used instead of viewform
url = 'googleformurl/formResponse'

def get_values():
    values_list = []
    now = datetime.datetime.now()
    day_name = now.strftime("%A")

    date = str(now).split('-')

    values = {
        # Last Name
         "entry.1774846002": str(sys.argv[1]),
        # First Name
        "entry.739431278": str(sys.argv[2]),
        # Grade
        "entry.640899473": str(sys.argv[3]),
    }

    values_list.append(values)
    print(values_list)
    return values_list


def send_attendance(url, data):
    """It takes google form url which is to be submitted and also data which is a list of data to be submitted in the form iteratively."""

    for d in data:
        try:
            requests.post(url, data=d)
            print("Form Submitted.")
            time.sleep(2)
        except:
            print("Error Occured!")


final_data = get_values()

send_attendance(url, final_data)
