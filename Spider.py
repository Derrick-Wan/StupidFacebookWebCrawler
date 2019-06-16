from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymysql
import re
import hashlib
import emoji

i = 1
db = pymysql.connect("120.78.148.41", "root", "Wanzy19981222", "FacebookData", use_unicode=True, charset="utf8")
cursor = db.cursor()


def Exist(href):
    cursor.execute("select 1 from facebookInfo where hash = '%s' limit 1" % href)
    exist = cursor.fetchall()
    if exist:
        return True
    else:
        return False


def get_elements():
    url = hashlib.sha256()
    href = browser.find_elements_by_xpath('//a[@class="_3084"]')
    nickname = browser.find_elements_by_xpath('//div[@class="_lic"]')
    content = browser.find_elements_by_xpath('//div[@class="_4rmu"]/div[1]')
    P_time = browser.find_elements_by_xpath('//span[@class = "timestampContent"]/..')
    like = browser.find_elements_by_xpath('//div[@class="_78j_"]')
    commentshare = browser.find_elements_by_xpath('//div[contains(@class,"_78k7")]')

    if len(href) == len(nickname) == len(content) == len(P_time) == len(like) == len(commentshare):
        for i in range(len(href)):
            href_t = href[i].get_attribute("href")
            url.update(href_t.encode())
            nickname_t = nickname[i].text.replace("'", "")
            content_t = (content[i].text).replace("\n", "").replace("'", "")
            P_time_t = P_time[i].get_attribute("title")
            like_t = like[i].text
            like_t = like_t.replace("\n", " ")
            like_t = like_t.split()
            commentshare_t = commentshare[i].text
            Comments = re.findall(r'(\d.{0,5}?) Comment', commentshare_t)
            Share = re.findall(r'(\d.{0,5}?) Share', commentshare_t)
            print(url.hexdigest(), href_t, nickname_t, content_t, P_time_t, like_t, Comments, Share)
            if len(Comments) == 0:
                Comments.append("0")
            if len(Share) == 0:
                Share.append("0")
            if len(like_t) == 0:
                like_t.append("0")
            content_t = emoji.demojize(content_t)
            nickname_t = emoji.demojize(nickname_t)
            if not Exist(url.hexdigest()):
                sql = "INSERT INTO facebookInfo(hash,URL,Nickname,publish,time,likes,comment,share)VALUES" \
                      "('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                          str(url.hexdigest()), href_t, nickname_t, content_t, P_time_t, like_t[0], Comments[0],
                          Share[0])
                try:
                    cursor.execute(sql)
                except pymysql.err.InternalError:
                    print(str(i) + " Miss")
                    i += 1
            else:
                print("Already exist.")
    else:
        print('href ', len(href), 'nickname ', len(nickname), 'content ', len(content), 'P_time ', len(P_time), 'like ',
              len(like), 'commentshare ', len(commentshare))
        browser.get("http://www.Facebook.com")
        searchField = browser.find_element_by_xpath('//input[@aria-label="Search"]')
        searchField.send_keys(topic)
        submit = wait.until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-testid="facebar_search_button"]')))
        # submit = browser.find_element_by_xpath()
        submit.click()
        Posts = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]')))
        Posts.click()
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        ViewAll = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Public Posts")]/../a')))
        ViewAll.click()
        for i in range(30):
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1)
            print(str(i) + "rounds")
        get_elements()


topics = ["cyberattack", "cyber security", "cyber hacking", "cyber hackers", "cyber hack"
                                                                             "network security", "network attack",
          "network hack", "network hacking", "network hacking", "network hackers"]
options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}

options.add_experimental_option('prefs', prefs)
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
wait = WebDriverWait(browser, 10)
browser.get("http://www.Facebook.com")
input = browser.find_element_by_name("email")
password = browser.find_element_by_name("pass")
input.send_keys("921951162@qq.com")
password.send_keys("chinaboy")
submit = browser.find_element_by_xpath('//label[@id="loginbutton"]')
submit.click()
for topic in topics:
    searchField = browser.find_element_by_xpath('//input[@aria-label="Search"]')
    searchField.send_keys(topic)
    submit = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@data-testid="facebar_search_button"]')))
    # submit = browser.find_element_by_xpath()
    submit.click()
    Posts = wait.until(EC.presence_of_element_located(
        (By.XPATH, '//body/div[1]/div[3]/div[1]/div/div[2]/div/div/div/div/div/div/div/div/ul/li[2]')))
    Posts.click()
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    ViewAll = wait.until(EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"Public Posts")]/../a')))
    ViewAll.click()
    for i in range(25):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
        print(str(i) + "rounds")
    get_elements()
    db.commit()
    browser.get("http://www.Facebook.com")

db.close()
browser.close()
