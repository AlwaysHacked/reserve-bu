# to kill 'trailing' browsers ->
# ps aux | grep firefox | grep child
# kill -9 (ps aux | grep firefox | grep child | cut -f8 -d' ' )

import argparse
from sys import exit
import signal

import Reserve
import Calendar

def handler(sig, frame) -> None:
	browser.quit()
	exit(1)

parser = argparse.ArgumentParser()

parser.add_argument("--show", "-s",		help="Show places", action="store_true")
parser.add_argument("--date", "-d",		help="Day of reservation, format: Y/M/D", default="tomorrow")
# parser.add_argument("--range","-D", help="Reservation for several days")
parser.add_argument("--reserve", '-r', 	help="Reserve, format: Room Time Duration ex: 11  09:00 2:30",
					nargs='*')
# parser.add_argument("--hour", "-H", 	help="Choose a place by hour, format: 9:00 2:30")
# parser.add_argument("--room", "-R", 	help="Room number", type=int)
# parser.add_argument("-t",  				help="Room number", type=str, nargs='*',)
args = parser.parse_args()
# parser.print_help()
# if not args.date:
# 	print("Need a date to look for")
# 	exit(1)
# else:
# 	print("Chosen date is %s" % args.date)
# if args.t:
# 	print(args.t)
	# exit(0)


day = Calendar.stringToDate(args.date)
if not Calendar.isValid(day):
	print("Given day is sunday, the BU is closed")
	exit(2)

browser = Reserve.setBrowser()
signal.signal(signal.SIGINT, handler)

if args.show:
	print("In show, looking place for: " + str(day))
	Reserve.showAvailPlaces(browser, day)

if args.reserve:
	r = args.reserve#.split()
	room = int(r[0])
	hour = r[1]
	duration = r[2]
	# print(r, room, hour, duration)
	Reserve.reserve(browser, day, room, hour, duration)

browser.quit()
exit(0)
