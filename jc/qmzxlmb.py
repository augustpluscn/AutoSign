from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import configparser

# 絢麗緬北公益站,自动签到

if __name__ == "__main__":
    name = 'qmzxlmb'
    config = configparser.ConfigParser()
    config.read('../config.ini')
    acc = config[name]['acc']
    psd = config[name]['psd']

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(
        'D:/tools/chromedriver/chromedriver.exe', chrome_options=chrome_options)
    browser.get('https://qmzxlmb.ml/#/auth/login')

    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[1]/input').send_keys(acc)
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[2]/div/div[2]/div[2]/div[2]/input').send_keys(psd)
    browser.find_element_by_xpath('//*[@id="login"]').click()
    time.sleep(10)
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[5]/div/div[2]/button').click()
    time.sleep(2)
    browser.find_element_by_xpath(
        '//*[@id="app"]/div/div[5]/div/div[1]/button').click()
    time.sleep(5)
    browser.close()
