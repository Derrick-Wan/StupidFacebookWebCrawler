from selenium import webdriver
import pymysql
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()

browser.get("http://www.Facebook.com")
input = browser.find_element_by_name("email")
password = browser.find_element_by_name("pass")
input.send_keys("921951162@qq.com")
password.send_keys("chinaboy")
submit = browser.find_element_by_xpath('//label[@id="loginbutton"]')
submit.click()
searchField = browser.find_element_by_xpath('//input[@aria-label="Search"]')
searchField.send_keys("cyber attack")
submit = browser.find_element_by_xpath('//button[@data-testid="facebar_search_button"]')
submit.click()
time.sleep(4)
href = browser.find_element_by_xpath('//body/div[1]/div[3]/div[1]/div/div[3]/div[2]/div/div/div[3]/div/div/div/div[2]'
                                     '/div/div/div[3]/div/div/div/div/div[1]/a').get_attribute("href")
browser.get(href)

# List =  browser.find_elements_by_xpath('//body/div/div[3]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div')
# while i < 50:
#     try :
#         print(List[i])
#         i += 1
#     except:
#         browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
#         newList =  browser.find_elements_by_xpath('//body/div/div[3]
#         /div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div')
#         print(newList[-1])
#         i += 1


for i in range(50):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)
    print(str(i) + "rounds")
List = browser.find_elements_by_xpath('//body/div/div[3]/div/div/div[3]/div[2]/div/div/div[2]/div/div/div/div')
for i in range(50):
    print(List[i])


db = pymysql.connect("localhost", "root", "Wanzy19981222", "facebook")
cursor = db.cursor()
db.close()
browser.close()
