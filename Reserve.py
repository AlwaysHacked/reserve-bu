import Calendar
from Availabilities import *

from bs4 import BeautifulSoup as bs

from sys import exit
from time import sleep
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

link = "https://affluences.com/bu-orsay/reservation?type=1&date="
email = "seryozha.hakobyan@u-psud.fr"
aval = Availabilities()

def setBrowser():
	options = Options()
	# options.add_argument("-headless")
	drive = wd.Firefox(options=options, executable_path="/home/serge/projects/geckodriver")
	drive.set_page_load_timeout(10)
	drive.implicitly_wait(10)
	return drive

# def loadPage(browser, link: str) -> None:
# 	run = True
# 	tries = 0
# 	while run and tries < 5:
# 		try:
# 			browser.get(link + str(day))
# 			run = False
# 		except:
# 			tries += 1
# 			print("Failed to load page, refreshing")
#
# 	if tries == 5 :
# 		print("Problem connecting to the website, please try later")
# 		exit(3)


def showAvailPlaces(browser, day) -> None:
	global aval
	run = True
	tries = 0
	while run and tries < 5:
		try:
			browser.get(link + str(day))

			run = False
		except:
			tries += 1
			print("Failed to load page, refreshing")

	if tries == 5 :
		print("Problem connecting to the website, please try later")
		browser.quit()
		exit(3)

	aval.add(browser.page_source)
	aval.show(day)

def roomNum(num : int) -> int:
	if num == 1:
		return 0
	elif num == 10:
		return 1
	elif num == 11:
		return 2
	return num + 1

def click(button) -> None:
	run = True
	i = 0
	while run:
		try:
			# page waits for some interaction before letting clicking on page
			# we will just go down on page :)
			button.send_keys(Keys.PAGE_DOWN)
			button.click()
			run = False
		except:
			print(i)
			i +=1
			pass

def reserve(browser, day, room: int, hour: str, duration: str) -> None:
	global aval
	# browser.get(link + str(day))
	# print(aval.rooms)
	# aval.add(browser.page_source)
	pos = aval.posInList(room, hour)
	if not aval.isAvailable(room, hour, duration):
		return

	num = roomNum(room)
	click(browser.find_elements(By.XPATH, '//button[normalize-space()="%s"]' % hour)[num])
	click(browser.find_elements(By.XPATH, '//button[normalize-space()="Book"]')[num])

	sleep(1)

	browser.find_element(By.ID, "email").send_keys(email)
	browser.find_elements(By.CLASS_NAME, "mat-checkbox-layout")[-1].click()
	click(browser.find_element(By.XPATH,'//button[normalize-space()="Book"]'))
