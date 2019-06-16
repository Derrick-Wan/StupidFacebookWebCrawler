import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import hashlib
import pymysql


def get_page(cursor, href):
    Posts = wait.until(EC.presence_of_element_located((By.XPATH, '//span[contains(text(),"Posts")]'))).click()
    t = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@data-testid="post_message"]')))
    for i in range(5):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(5)
        print(str(i) + "rounds")
    # 开始爬取
    content = browser.find_elements_by_xpath('//div[@data-testid="post_message"]/p[contains(text(),"Cyber")]/..')
    name = browser.find_element_by_xpath('//span[@class="fwb fcg"]').text
    for i in range(len(content)):
        try:
            content_t = (content[i].text).replace("\\", "").replace("'", "")
            time2 = content[i].find_element_by_xpath(
                '..//a[@class="_5pcq"]//span[@class = "timestampContent"]/..').get_attribute("title")
            likecommentshare = content[i].find_element_by_xpath('../../../..//div[@class="_4299"]').text
            like_t = re.findall(r'(\d.{0,5}?)\n', likecommentshare)
            comment = re.findall(r'(\d.{0,5}?) Comment', likecommentshare)
            share = re.findall(r'(\d.{0,5}?) Share', likecommentshare)
            hashnum = hashlib.sha256()
            hashnum.update(content[i].text.encode())
            print('hash', hashnum.hexdigest(), 'href', href, 'pagesname', name, 'content', content_t.encode(), 'time',
                  time2, 'like', like_t, 'comment', comment, 'share', share)

        except:
            break
        if len(like_t) == 0:
            like_t.append("0")
        if len(comment) == 0:
            comment.append("0")
        if len(share) == 0:
            share.append("0")
        sql = "INSERT INTO one_hundred(hash,URL,Nickname,publish,time,likes,comment,share)VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
        str(hashnum.hexdigest()), href, name, content_t, time2, like_t[0], comment[0], share[0])
        try:
            cursor.execute(sql)
        except:
            pass
        del hashnum


options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_setting_values':
        {
            'notifications': 2
        }
}
options.add_experimental_option('prefs', prefs)
browser = webdriver.Chrome(chrome_options=options)
wait = WebDriverWait(browser, 10)
browser.get("http://www.Facebook.com")
input = browser.find_element_by_name("email")
password = browser.find_element_by_name("pass")
input.send_keys("921951162@qq.com")
password.send_keys("chinaboy")
submit = browser.find_element_by_xpath('//label[@id="loginbutton"]')
submit.click()

time.sleep(3)
# 100个 特·定 用户
'''
www=['https://www.facebook.com/ascyberwargames/?ref=br_rs', 'https://www.facebook.com/Cyber2.0Defense/?ref=br_rs',
     'https://www.facebook.com/Cyber-Attack-Insurance-272137063432762/?ref=br_rs', 'https://www.facebook.com/TeamCyberEvo/?ref=br_rs',
     'https://www.facebook.com/CyberArk/?ref=br_rs', 'https://www.facebook.com/cyberoctopuses/?ref=br_rs', 'https://www.facebook.com/BreakingCyberSecNews/?ref=br_rs',
     'https://www.facebook.com/ICSScompany/?ref=br_rs', 'https://www.facebook.com/kumarro2703/?ref=br_rs', 'https://www.facebook.com/Cymulate/?ref=br_rs',
     'https://www.facebook.com/Cyber-Attack-Squad-1614374852107720/?ref=br_rs', 'https://www.facebook.com/CyberAttack-Stories-689618441476647/?ref=br_rs',
     'https://www.facebook.com/CyberSwarmInc/?ref=br_rs', 'https://www.facebook.com/cybersecinstitute/?ref=br_rs', 'https://www.facebook.com/gbhackersadmin/?ref=br_rs',
     'https://www.facebook.com/Cyberint/?ref=br_rs', 'https://www.facebook.com/NCSByHTCS/?ref=br_rs',
     'https://www.facebook.com/xmcyber/?ref=br_rs','https://www.facebook.com/CyberHubEngage/?ref=br_rs','https://www.facebook.com/CyberTracksOfficial/?ref=br_rs','https://www.facebook.com/SeconCyber/?ref=br_rs',
     'https://www.facebook.com/cyberfortechno/?ref=br_rs','https://www.facebook.com/Cyber-war-479626402219324/?ref=br_rs','https://www.facebook.com/Attack-On-the-Cyber-World-1162513397106409/?ref=br_rs',
     'https://www.facebook.com/cyberstrikeband/?ref=br_rs','https://www.facebook.com/xmcyber/?ref=br_rs','https://www.facebook.com/CyberHubEngage/?ref=br_rs',
     'https://www.facebook.com/CyberTracksOfficial/?ref=br_rs','https://www.facebook.com/SeconCyber/?ref=br_rs','https://www.facebook.com/CyberEngineering/?ref=br_rs',
     'https://www.facebook.com/Cyber-Warfare-143350125709114/?ref=br_rs','https://www.facebook.com/Cyber-war-479626402219324/?ref=br_rs','https://www.facebook.com/cyberstrikeband/?ref=br_rs',
     'https://www.facebook.com/Attack-On-the-Cyber-World-1162513397106409/?ref=br_rs','https://www.facebook.com/CyberDefenses/?ref=br_rs','https://www.facebook.com/Cyber-Steve-836561556434322/?ref=br_rs',
     'https://www.facebook.com/FamilyAttackCyberOfficial/?ref=br_rs','https://www.facebook.com/deuserrorcyberteamattack/?ref=br_rs','https://www.facebook.com/Team-Cyber-Attack-Makassar-309687623230771/?ref=br_rs',
     'https://www.facebook.com/Cyber-Attack-Squad-1614374852107720/?ref=br_rs','https://www.facebook.com/Cyberint/?ref=br_rs','https://www.facebook.com/CyberSwarmInc/?ref=br_rs',
     'https://www.facebook.com/staysafeonline/?ref=br_rs','https://www.facebook.com/cyagency/?ref=br_rs','https://www.facebook.com/Hackingtutorialsandnews/?ref=br_rs',
     'https://www.facebook.com/cyberctdmp/?ref=br_rs','https://www.facebook.com/kumarro2703/?ref=br_rs','https://www.facebook.com/BreakingCyberSecNews/?ref=br_rs',
     'https://www.facebook.com/NCSByHTCS/?ref=br_rs','https://www.facebook.com/advcybsec/?ref=br_rs','https://www.facebook.com/CertifiedEC/?ref=br_rs',
     'https://www.facebook.com/CyberSecurityMalaysia/?ref=br_rs','https://www.facebook.com/cybersecurjobs/?ref=br_rs',
     'https://www.facebook.com/Hackingtutorialsandnews/?ref=br_rs','https://www.facebook.com/ethicalhackingnewsandtutorials/?ref=br_rs','https://www.facebook.com/PhilipineCyberHacking.gov/?ref=br_rs',
     'https://www.facebook.com/gbhackersadmin/?ref=br_rs','https://www.facebook.com/pakhackingforum/?ref=br_rs','https://www.facebook.com/CyberHackLPU/?ref=br_rs',
     'https://www.facebook.com/CEH.CyberHacker/?ref=br_rs','https://www.facebook.com/cyberhackinthewold/?ref=br_rs','https://www.facebook.com/staysafeonline/?ref=br_rs',
     'https://www.facebook.com/PakCyberThunders/?ref=br_rs','https://www.facebook.com/CyberHackerGame/?ref=br_rs','https://www.facebook.com/Cyber-Hack-1389932484562273/?ref=br_rs',
     'https://www.facebook.com/IHCTIND/?ref=br_rs','https://www.facebook.com/CyberTechCommunication/?ref=br_rs','https://www.facebook.com/cybertechza/?ref=br_rs',
     'https://www.facebook.com/CyberTechOnline/?ref=br_rs','https://www.facebook.com/CyberTechIsrael/?ref=br_rs','https://www.facebook.com/CyberTechKaraoke/?ref=br_rs',
     'https://www.facebook.com/cybertechph/?ref=br_rs','https://www.facebook.com/Cybertech.Singapore/?ref=br_rs','https://www.facebook.com/cybertech4u/?ref=br_rs',
     'https://www.facebook.com/cybertechwebsolution/?ref=br_rs','https://www.facebook.com/CT.YTo/?ref=br_rs','https://www.facebook.com/cybertechsolution/?ref=br_rs',
     'https://www.facebook.com/cybertechsolution/?ref=br_rs','https://www.facebook.com/CyberTech-Software-121691954579896/?ref=br_rs','https://www.facebook.com/Cyber-Tech-2115672475161621/?ref=br_rs',
     'https://www.facebook.com/CyberTech-Repair-Center-1052124844814896/?ref=br_rs','https://www.facebook.com/cybertechko/?ref=br_rs','https://www.facebook.com/cybertechulbs/?ref=br_rs',
     'https://www.facebook.com/ct.cybertech/?ref=br_rs','https://www.facebook.com/cybertechmalawi/?ref=br_rs','https://www.facebook.com/CyberTech-279709435416634/?ref=br_rs',
     'https://www.facebook.com/CYBER-TECH-1645822439029120/?ref=br_rs','https://www.facebook.com/sapphirelove57/?ref=br_rs','https://www.facebook.com/EnrichNetzone/?ref=br_rs',
     'https://www.facebook.com/cybernetwark/?ref=br_rs','https://www.facebook.com/CyberNetworkLTD/?ref=br_rs','https://www.facebook.com/CyberFM/?ref=br_rs',
     'https://www.facebook.com/cybertronns/?ref=br_rs','https://www.facebook.com/cynetdef/?ref=br_rs','https://www.facebook.com/mdccabletv/?ref=br_rs',
     'https://www.facebook.com/TheCyberLeadersNetwork/?ref=br_rs',


'''

www = ['https://www.facebook.com/ICSScompany/?ref=br_rs'
       'https://www.facebook.com/cybernetwark/?ref=br_rs', 'https://www.facebook.com/CyberNetworkLTD/?ref=br_rs',
       'https://www.facebook.com/EnrichNetzone/?ref=br_rs',
       'https://www.facebook.com/cynetdef/?ref=br_rs', 'https://www.facebook.com/mdccabletv/?ref=br_rs',
       'https://www.facebook.com/CyberFM/?ref=br_rs',
       'https://www.facebook.com/CybernetworksAUS/?ref=br_rs', 'https://www.facebook.com/ICSScompany/?ref=br_rs',
       'https://www.facebook.com/cybertronns/?ref=br_rs'
       ]
# 启动数据库
db = pymysql.connect("120.78.148.41", "root", "Wanzy19981222", "FacebookData", use_unicode=True, charset="utf8")
cursor = db.cursor()

for i in range(len(www)):
    js = 'window.open("' + www[i] + '");'
    browser.execute_script(js)
    allHandles = browser.window_handles
    browser.switch_to_window(allHandles[1])
    #
    get_page(cursor, www[i])
    browser.close()
    browser.switch_to_window(allHandles[0])
    db.commit()

db.close()
browser.close()
