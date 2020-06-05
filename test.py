# this text is running in sublime text 3

from selenium import webdriver
from loginDetails import LoginDetails as ld
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import argparse
import json
from bs4 import BeautifulSoup as bs
import requests
from lxml import html

class MMLSBot():

	stateWebBrowser = False
	locationStatus = 0 # represents main page , register subject 1 , finance 2 , attendance report 3 , 

	def __init__(self):
		ld.login_id_pass()
		firefoxPath = "/home/mint/Desktop/geckodriver"
		self.driver = webdriver.Firefox(executable_path=firefoxPath)
		self.driver.set_window_size(1024, 768)
		self.frameinMMLS = 'ptifrmtgtframe' # for switching frame later

		

	def login(self):
		website = self.driver.get(ld.ocmsURL)
		loginOCMS = self.driver.find_element_by_xpath("//input[@id='userid']")
		loginOCMS.send_keys(ld.username)

		passOCMS = self.driver.find_element_by_xpath("//input[@id='pwd']")
		passOCMS.send_keys(ld.password)

		loginButton = self.driver.find_element_by_xpath("//input[contains(@class, 'psloginbutton')]")
		loginButton.click()

	def base_academics(self):

		self.login()

		sleep(2)

		selfService_link = self.driver.find_element_by_link_text('Self Service')
		selfService_link.click()

		sleep(2)

		self.driver.switch_to.frame(self.frameinMMLS) # switch to the iframe inside

		academic_link = self.driver.find_element_by_xpath("//a[contains(text(), 'Academics')]")
		academic_link.click()

	def base_finance(self):

		self.login()

		sleep(2)

		selfService_link = self.driver.find_element_by_link_text('Self Service')
		selfService_link.click()

		sleep(2)

		self.driver.switch_to.frame(self.frameinMMLS) # switch to the iframe inside

		academic_link = self.driver.find_element_by_link_text('Account Activity')
		academic_link.click()



	def registerSubject(self):
		self.base_academics()

		sleep(2)

		course_enrol_link = self.driver.find_element_by_link_text('Course Enrollment')
		course_enrol_link.click()

		sleep(2)

		add_class_link = self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr[2]/td/table/tbody/tr/td[3]/table/tbody/tr/td/table/tbody/tr[2]/td/ul/li[3]/a')
		add_class_link.click() # this is dangerous is the structure changes , add table as parent would be bettter



	def finance(self):

		self.base_finance()
		sleep(2)
		finance_link = self.driver.find_element_by_link_text('Account Enquiry')
		finance_link.click()


		return 0

	def attendance(self):
		self.base_academics()
		sleep(2)

		attendance_link = self.driver.find_element_by_link_text('Attendance Report')
		attendance_link.click()

		sleep(2)
		attendance_report_link = self.driver.find_element_by_link_text('Attendance Percentage by class')
		attendance_report_link.click()



	def checkAdvisor(self):
		self.base()
		sleep(2)

		academic_records_link =  self.driver.find_element_by_link_text('Academic Records')
		academic_records_link.click()

		advisor_link = lf.driver.find_element_by_link_text('My Advisors')
		advisor_link.click()


	def timetable(self):

		#headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:76.0) Gecko/20100101 Firefox/76.0'}
		with requests.Session() as s:

				login_data = {
					'timezoneOffset': -480,
			    	'userid': ld.username,
			    	'pwd': ld.password
				}

				headers = {
					'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:76.0) Gecko/20100101 Firefox/76.0'
				}



				url = 'https://cms.mmu.edu.my/?cmd=login&languageCd=ENG'

				urlTimetable = 'https://cms.mmu.edu.my/psp/csprd/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_LIST.GBL?PORTALPARAM_PTCNAV=HC_SSR_SSENRL_LIST&EOPP.SCNode=HRMS&EOPP.SCPortal=EMPLOYEE&EOPP.SCName=CO_EMPLOYEE_SELF_SERVICE&EOPP.SCLabel=Course%20Enrollment&EOPP.SCFName=N_NEW_CRSENRL&EOPP.SCSecondary=true&EOPP.SCPTfname=N_NEW_CRSENRL&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE.N_NEW_ACADEMICS.N_NEW_CRSENRL.N_NEW_CLASSSCH.HC_SSR_SSENRL_LIST&IsFolder=false'

				post  = s.post(url, data=login_data , headers = headers )
				print(post.text)

				timetable = s.get(urlTimetable , headers = headers)
				print(timetable.text)





			



	def backpage(self):
		# due to DOM Manipulation
		self.driver.switch_to.default_content()#window_handles)
		sleep(2)
		self.driver.back() #execute_script("window.history.go(-1)")



def input():
	parser = argparse.ArgumentParser()
	parser.add_argument("-start" , help = 'Execute Browser' , action="store_true")
	parser.add_argument("-rs" , help = 'Register Subject.' , action="store_true")
	parser.add_argument("-f" , help = 'Check finance.' ,action="store_true") 
	parser.add_argument("-ad" , help = 'Check advisor.',action="store_true") 
	parser.add_argument("-at" , help = 'Check attendance.',action="store_true")
	
	args = parser.parse_args()
		
	arguments = vars(args)
	return arguments

def main():
	value = input()
		

	if value['start'] & value['rs']:
		print('Launch bot')
		print("Registering subject.")
		bot = MMLSBot()
		bot.registerSubject()
	elif value['start'] & value['f']:
		print('Launch bot')
		print("Checking finance.")
		bot = MMLSBot()
		bot.finance()
	elif value['start'] & value['ad']:
		print('Launch bot')
		print("Checking your advisor.")
		bot = MMLSBot()
		bot.checkAdvisor()
	elif value['start'] & value['at']:
		print('Launch bot')
		print("Checking your attendance.")
		bot = MMLSBot()
		bot.attendance()
	else:
		print('No arguement pass.')
		print('pass -h in the CLI for more info.')

 




if __name__ == "__main__":

	main()

	






'''
  for  future instance the need of handling pop-up
  Alert a = driver.switchTo().alert();
	a.confirm();
'''