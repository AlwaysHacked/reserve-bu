from printing import *

import requests
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
			room = r.find(class_="color-affluences-blue-dark").text
			room = room.split()[-1][2:]
			self.rooms.update({room : []})
			hourButtons = r.find(class_="hour-grp")
			try:
				hours = hourButtons.find_all(class_="hour")
				for h in hours:
					dis = "unavailable" not in str(h)
					self.rooms[room].append((h.text, dis))
			except:
				print("No available places :(")
				return

	def show(self, date) -> None:
		print(date)
		for r in self.rooms:
			printtitle("Salle de travail numéro : " + r)
			print()

			for h in self.rooms[r]:
				if h[1]:
					printActiveButton(h[0])
				else:
					printInactiveButton(h[0])

			print('\n')

	def creneauxDaffiles():
		return None

	def posInList(self, num: int, hour: str):
		pos = 0
		for i in self.rooms	:
			if int(i) == num:
				break
			if hour in self.rooms[i]:
				pos += 1
		return pos
	# def showByHour(self, h, d):






#
