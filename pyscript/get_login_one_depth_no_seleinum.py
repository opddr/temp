#-*- coding:utf-8 -*-

import csv
import requests
import time
from bs4 import BeautifulSoup
import re
import time
import copy
import urllib.parse as urlparse
import sys
default_delay = 0.3

request_header = {
	"Accept": "*/*",
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac Os X 10_9_5) AppleWebKit 537.36 (KHMTL, like Gecko) Chrome',
	'Accept-Language': 'ko-KR,ko;q=0.8,en-US;q=0.6,en;q=0.4',
	'Content-Type': 'text/html; charset=utf-8'
}

target_url = "http://www.business.kaist.ac.kr/"

class test():

	filename = "test.csv"
	def __init__(self,autoexit=False):

		if autoexit:
			os.system('taskkill /F /IM chromedriver.exe & taskkill /F /IM chrome.exe')
		
		try:
			item_list = self.read_csv(self.filename)
			for item in item_list:
				if not item_list:
					continue
				print(item[0])
				for test in self.get_url(item[1]):
					print("후보 : ", urlparse.urljoin(item[1], test))
				print('---------')
				

		except KeyboardInterrupt:
			print('Keyboard interrupt caught testsetsetset')
			self.auto_exit()
			#workbook.close()	
			print("workbook closed")
		except MyError as err:
			print("Hiccup:",err)
			print("quit")
			self.auto_exit()
			#workbook.close()	
			print("workbook closed")
		self.auto_exit()

		print("final quit")

	def get_url(self,url):

		try:
			html = requests.get(url,headers=request_header,verify=False)

			bs_obj = BeautifulSoup(html.text,'html.parser')
			a_candidate = bs_obj.select('a')
			a_success = []
			for one in a_candidate:
				if one.get('href') and (('login' in one['href'].lower() or '로그인' in one['href']) or ('login' in one.get_text().lower() or '로그인' in one.get_text())):
					a_success.append(one['href'])
			return a_success
		except Exception as e:

			print(e)
			return []

		
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


	def auto_exit(self):

		print("exiting..")
		
		exit(1)




if __name__ == '__main__':

	if len(sys.argv)==2:
		if sys.argv[1].lower() == 'exit':
			test(autoexit=True)
		else:
			test()
	else:
		test()
