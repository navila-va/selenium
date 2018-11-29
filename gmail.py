from selenium import webdriver
import time
driver=webdriver.Chrome('C:\\chromedriver.exe')
#x.close()
driver.get("http:\\www.gmail.com")
driver.maximize_window()
driver.find_element_by_css_selector("[id='identifierId']").send_keys('malekabegum1968')
#time.sleep(5)
driver.find_element_by_css_selector("[id='identifierNext']").click()
time.sleep(5)
driver.find_element_by_css_selector("[name='password']").send_keys('navilaalam95')
time.sleep(5)

#x.close()

driver.find_element_by_css_selector("[id='passwordNext']").click()
time.sleep (5)
driver.find_element_by_css_selector("[class='z0'] [class='T-I J-J5-Ji T-I-KE L3']").click()
#x.maximize_window()
to_button=driver.find_element_by_css_selector("[class='nH Hd'][role='dialog'] textarea[name='to']")
to_button.click()
#to_button.send_keys('niranjandas25@gmail.com')
#to_button.send_keys('malekabegum1968@gimail.com')
#to_button.send_keys('kamalfatima366@gmail.com')
to_button.send_keys('malekabegum1968@gmail.com')
#time.sleep(10)
subjectbox=driver.find_element_by_css_selector("[name='subjectbox']")
subjectbox.send_keys('Selenium')
#subjectbox = x.find_element_by_css_selector("[class='nH Hd'][role='dialog'] input[name='subjectbox']")
#subjectbox.click()
#subjectbox.send_keys('niranjandas 25')
body=driver.find_element_by_css_selector("[class='nH Hd'][role='dialog'] table[class='cf An'] div[aria-label='Message Body']")
body.click()
body.send_keys('test')

driver.find_element_by_css_selector("[class='nH Hd'][role='dialog'] div[data-tooltip^='Send']").click()
#x.find_element_by_css_selector("[class='gb_b gb_fb gb_R']").click()

#x.find_element_by_css_selector("[class = 'aio UKr6le']").click()
time.sleep(5)
rows=driver.find_elements_by_css_selector("tr[class='zA zE']")
for elem in rows:
    if 'maleka' in elem.text:
        print('Your test is PASS')
        break
    else:
        print("Your test is FAIL")

#driver.close()


driver.find_element_by_css_selector("[class='gb_ab gbii']").click()
driver.find_element_by_css_selector ("[class='gb_za gb_dg gb_jg gb_Ze gb_Hb']").click()
