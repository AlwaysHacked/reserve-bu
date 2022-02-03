# from datetime import datetime.date, datetime.timedelta
import datetime

format = "%Y-%m-%d"

def daterange(start_date, end_date):
	dates = []
	for n in range(int((end_date - start_date).days)):
		d = start_date + datetime.timedelta(n)
		if not d.weekday() == 6 : # skipping sundays
			dates.append(d.strftime(format))
	return dates

def today():
	return datetime.date.today()#.strftime(format)

def tomorrow():
	return (datetime.date.today() + datetime.timedelta(1))#.strftime(format)

# def tomorrow():


def week():
	for i in range(7):
		if((datetime.date.today() + datetime.timedelta(i)).weekday() == 5) : # checks till saturday
			return daterange(datetime.date.today(), datetime.date.today() + datetime.timedelta(i))

def stringToDate(s : str):
	if(s == "today" or s == "Today" or s == "TODAY"):
		return today()
	if(s == "tomorrow" or s == "Tomorrow" or s == "TOMORROW"):
		return tomorrow()
	if(s == "week" or s == "Week" or s == "WEEK"):
		return week()

	s = s.split('/')
	return datetime.date(int(s[0]), int(s[1]), int(s[2]))

def stringToHour(s : str):
	'''@arg format : "9:30 2:30"'''
	h, d = s.split()
	# les creneaux proposes sur le site sont de 30 min
	# on pourrait donc regarder combien de 30 min on veut
	# en convertant `d` en minutes / 30
	d = d.split(':')
	d = (int(d[0]) * 60) / 30 + int(d[1])

def isValid(d : datetime.date) -> bool:
	return d.weekday() != 6 # is not a sunday
