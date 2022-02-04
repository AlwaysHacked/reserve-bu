import Calendar
from Availabilities import *

from sys import exit
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

link = "https://affluences.com/bu-orsay/reservation?type=1&date="
email = "seryozha.hakobyan@u-psud.fr"
aval = Availabilities()

def setBrowser():
	options = Options()
	options.add_argument("-headless")
	drive = wd.Firefox(options=options, executable_path="/home/serge/projects/geckodriver")
	return drive

def showAvailPlaces(browser, day) -> None:
	global aval
	if(Calendar.isValid(day)):
		browser.get(link + str(day))
		aval.add(browser.page_source)
		aval.show(day)
	else:
		print("Given date is a sunday, the BU is closed")
		exit(2)

def reserve(browser, day, numSalle: int, hour: str, duration: str) -> None:
	global aval
	browser.get(link + day)
	aval.add(browser.page_source)
	pos = aval.posInList(numSalle, hour)
	print(hour, pos)
	print(browser.find_elements(By.PARTIAL_LINK_TEXT, hour))#[pos].click()
	browser.find_elements(By.PARTIAL_LINK_TEXT, hour)[pos].click()
	browser.find_elements(By.PARTIAL_LINK_TEXT, duration)[pos].click()
	browser.find_elements(By.PARTIAL_LINK_TEXT, 'Book')[pos].click()
