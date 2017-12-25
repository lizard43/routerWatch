#!/usr/bin/python

import os

sites = ["google.com", "facebook.com", "s3.amazonaws.com"]

numPings = "3"  # number of pings per site
interval = "1"  # seconds between pings

# returning up means we could ping at least one internet site
# returning down means we could not ping any sites, we short circuit in this case as router needs to be restarted immediately


def checkUp():

    for site in sites:
        print("Pinging " + site)
        response = os.system("ping -c " + numPings + " -i " +
                             interval + " " + site + " 2>&1 >/dev/null")
        if response == 0:
            return "up"

    return "down"


if __name__ == '__main__':
    print checkUp()
