from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import configparser

# 樱花公益站,自动签到

if __name__ == "__main__":
    name = 'sakura'
    config = configparser.ConfigParser()
    config.read('./config.ini')
    acc = config[name]['acc']
    psd = config[name]['psd']

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    browser = webdriver.Chrome(
        'D:/tools/chromedriver/chromedriver.exe', chrome_options=chrome_options)
    browser.get('https://sakura.kozow.com/auth/login')
    time.sleep(10)
    browser.find_element_by_xpath(
        '//*[@id="email"]').send_keys(acc)
    browser.find_element_by_xpath(
        '//*[@id="passwd"]').send_keys(psd)
    browser.find_element_by_xpath(
        '//*[@id="login"]').click()
    time.sleep(10)

    flag = 0
    try:
        browser.find_element_by_xpath(
            '//*[@id="checkin"]').click()
        print("签到成功")
    except:
        flag = 1

    if flag == 1:
        try:
            browser.find_element_by_xpath(
                '//div[@class="usercheck pull-left"]/p/a')
            print("已经签到")
        except:
            print("签到失败")

    time.sleep(5)
    browser.close()
