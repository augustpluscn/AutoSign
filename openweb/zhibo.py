from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

if __name__ == "__main__":

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(
        'D:/tools/chromedriver/chromedriver.exe')
    browser.get('https://wx.vzan.com/live/tvchat-328425822?v=1594348316127')
    time.sleep(5)
    
    while 1==1:
        browser.refresh()
        time.sleep(2)
