#-*- coding:utf-8 -*-
from selenium import webdriver
from selenium import common 
from selenium.webdriver.common.alert import Alert
import csv
import requests
import time
from bs4 import BeautifulSoup
import re
import time
import copy
import sys
default_delay = 0.3

request_header = {
	"Accept": "*/*",
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac Os X 10_9_5) AppleWebKit 537.36 (KHMTL, like Gecko) Chrome',
	'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
	'Content-Type': 'text/html; charset=utf-8'
}

target_url = "http://www.business.kaist.ac.kr/"



#xpath query $x("//*[*[contains(translate(@href, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'login')]]")

class test():
		
	filename = "test.csv"
	def __init__(self,autoexit=False):

		if autoexit:
			os.system('taskkill /F /IM chromedriver.exe & taskkill /F /IM chrome.exe')
		driver = self.driver_start()
		try:
			item_list = self.read_csv(self.filename)
			if not item_list:
				self.auto_exit(driver)

			##3.toss url

			for item in item_list:

				print("name : {}".format(item[0]))
				tech_list = self.toss_url(item[1],driver)
				if not len(tech_list):
					print("url : none")
					continue
				for candi in tech_list:
					#print(candi)

					print("url :",candi.get_attribute('href'))
					
#					self.auto_exit(driver)

				print('---------------------')

			self.auto_exit(driver)
		except KeyboardInterrupt:
			print('Keyboard interrupt caught testsetsetset')
			self.auto_exit(driver)
			#workbook.close()	
			print("workbook closed")
		except MyError as err:
			print("Hiccup:",err)
			print("quit")
			self.auto_exit(driver)
			#workbook.close()	
			print("workbook closed")
		self.auto_exit(driver)

		print("final quit")

	def driver_start(self):

		#print(requests.get(self.login_url,headers=request_header))  # fresh cookies
		#webbrowser.open("https://google.com")
		options = webdriver.ChromeOptions()
		options.add_argument('headless')
		options.add_argument("disable-infobars")
		options.add_argument('--no-sandbox')
		options.add_argument("--disable-notifications")
		#options.add_argument("--disable-extensions")
		#options.add_argument('--disable-dev-shm-usage')

		path = 'chromedriver'

		driver = webdriver.Chrome(path,chrome_options=options)
		session_id = driver.session_id
		print("session_id :", session_id)
		
		driver.implicitly_wait(1)
		
		return driver

	def read_csv(self,filename):

		try:
			item_list = []
			with open(filename,'r',encoding='utf-8') as f:

				reader = csv.reader(f,delimiter=',')
				for item in reader:
					if len(item):
						item_list.append(item)
		except Exception as e:
			print(e)
			return
		return item_list

	def toss_url(self,url,driver):

		driver.get(url)
		return driver.find_elements_by_xpath("//a[contains(translate(@href, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'),'login')]") #/@href


	def auto_exit(self,driver):

		print("exiting..")
		driver.close()
		driver.quit()
		exit(1)





if __name__ == '__main__':

	if len(sys.argv)==2:
		if sys.argv[1].lower() == 'exit':
			test(autoexit=True)
		else:
			test()
	else:
		test()
