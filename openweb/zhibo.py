from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

if __name__ == "__main__":

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    browser = webdriver.Chrome(
        '/usr/local/chromedriver', chrome_options=chrome_options)

    browser.get('https://wx.vzan.com/live/tvchat-1286278451?shareuid=300126588#/')
    time.sleep(5)
    
    while 1==1:
        browser.refresh()
        time.sleep(2)
