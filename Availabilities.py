from printing import *

# import requests
from bs4 import BeautifulSoup as bs

class Availabilities:
	rooms: dict # dict -> {1 : [(09h00, False), (09h30, True)]}

	def __init__(self, d={}):
		self.rooms = d

	def add(self, page: str) -> None:
		# page = requests.get(link)
		soup = bs(page, "html.parser")
		rooms = soup.find_all(class_="mat-card")

		for r in rooms:
			try:
				room = r.find(class_="color-affluences-blue-dark").text
				room = int(room.split()[-1][2:]) # getting room's number

				if not room in self.rooms:
					self.rooms.update({room : []})

				hourButtons = r.find(class_="hour-grp")

				hours = hourButtons.find_all(class_="hour")
				for h in hours:
					dis = "unavailable" not in str(h)
					self.rooms[room].append((h.text.split()[0], dis))
			except:
				pass

	def show(self, date) -> None:
		print(date)
		for r in self.rooms:
			printtitle("Salle de travail numéro : %d" % r)
			print()

			for h in self.rooms[r]:
				if h[1]:
					printActiveButton(h[0])
				else:
					printInactiveButton(h[0])

			print('\n')

	def creneauxDaffiles():
		return None

	def isAvailable(self, room : int, hour : str, duration : str) -> bool:
		if(room in self.rooms):
			if((hour, True) in self.rooms.get(room)):
				return True
		return False

	def posInList(self, num: int, hour: str):
		pos = 0
		for i in self.rooms	:
			if int(i) == num:
				break
			if (hour, False) in self.rooms[i] or (hour, True) in self.rooms[i]:
				pos += 1
		return pos
	# def showByHour(self, h, d):






#
