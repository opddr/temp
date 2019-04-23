from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.implicitly_wait(3)

# 고려대학교 로그인 페이지
driver.get('https://korea.ac.kr/cop/member/memberLoginForm.do?siteId=university&id=university_090100000000')

driver.find_element_by_name('userId').send_keys('testtest')
driver.find_element_by_name('userPw').send_keys('11111111')

driver.find_element_by_xpath("//div[@class='login_box']//button[@type='submit']").click()