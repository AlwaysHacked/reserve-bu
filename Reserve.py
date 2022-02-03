import Calendar
from Availabilities import *

from sys import exit
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

link = "https://affluences.com/bu-orsay/reservation?type=1&date="
email = "seryozha.hakobyan@u-psud.fr"

# opt = wd.FirefoxOptions()
# opt.headless = 1
drive = wd.Firefox(executable_path="/home/serge/projects/geckodriver")#, options=opt)
aval = Availabilities()

def showAvailPlaces(day):
	global drive
	global aval
	if(Calendar.isValid(day)):
		drive.get(link + str(day))
		aval.add(drive.page_source)
		aval.show()
	else:
		print("Given date is a sunday, the BU is closed")
		exit(2)

def reserve(day, numSalle: int, hour: str, duration: str) -> None:
	global drive
	global aval
	drive.get(link + day)
	aval.add(drive.page_source)
	pos = aval.posInList(numSalle, hour)
	print(hour, pos)
	print(drive.find_elements(By.PARTIAL_LINK_TEXT, hour))#[pos].click()
	drive.find_elements(By.PARTIAL_LINK_TEXT, hour)[pos].click()
	drive.find_elements(By.PARTIAL_LINK_TEXT, duration)[pos].click()
	drive.find_elements(By.PARTIAL_LINK_TEXT, 'Book')[pos].click()
