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

baseurl = "https://search.naver.com/search.naver"
query = "https://search.naver.com/search.naver?&query=%EC%A0%84%EA%B5%AD+%EB%8C%80%ED%95%99%EA%B5%90"

html = requests.get(query)
bs_obj = BeautifulSoup(html.text,'html.parser')
result = []
for test in ((baseurl+item.a['href'],item.a.get_text().strip()) for item in (bs_obj.select_one('#main_pack > div.content_search.section > div > div.cs_produce > div.scroll').select('ul > li'))):
	
	ac_name_url = requests.get(test[0],headers=request_header)
	#time.sleep(default_delay)
	ac_url = BeautifulSoup(ac_name_url.content.decode('utf-8','replace'),'html.parser').select_one("#main_pack > div.sc.cs_university._cs_university_single > div.api_subject_bx > div.api_title_area > h3 > a")['href']
	result.append((test[1],ac_url))

with open('test3.csv','w') as f:

	writer = csv.writer(f,delimiter=',')
	for a,b in result:
		writer.writerow([a,b])
