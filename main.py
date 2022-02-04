# to kill 'trailing' browsers ->
# ps aux | grep firefox | grep child
# kill -9 (ps aux | grep firefox | grep child | cut -f8 -d' ' )

import argparse
from sys import exit
import signal

import Reserve
import Calendar

def handler(sig, frame):
	browser.quit()
	exit(1)

parser = argparse.ArgumentParser()

parser.add_argument("--show", "-s", help="Show places", action="store_true")
parser.add_argument("--date", "-d", help="Day of reservation, format: Y/M/D", default="tomorrow")
# parser.add_argument("--range","-D", help="Reservation for several days")
parser.add_argument("--hour", "-H", help="Choose a place by hour, format: 9:00 2:30")
parser.add_argument("--reserve", '-r', help="Reserve, format : 09:00 2:30")
parser.add_argument("--room", "-R", help="Room number", type=int)
# parser.add_argument("--help")
args = parser.parse_args()

# if not args.date:
# 	print("Need a date to look for")
# 	exit(1)
# else:
# 	print("Chosen date is %s" % args.date)
day = Calendar.stringToDate(args.date)
browser = Reserve.setBrowser()
signal.signal(signal.SIGINT, handler)

if args.show:
	Reserve.showAvailPlaces(browser, day)

elif args.reserve:
	hour = args.reserve.split()
	duration = hour[1]
	hour = hour[0]
	Reserve.reserve(browser, day, args.room, hour, duration)

browser.quit()
exit(0)
