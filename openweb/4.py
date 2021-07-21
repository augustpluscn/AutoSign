import requests
import time
import threading

def open():
    target = "https://wx.vzan.com/live/tvchat-1373773202#/"

    
    while 1==1:
        req = requests.get(url = target)
        req.encoding = 'utf-8'
        # print(req.text)
        time.sleep(2)


if __name__ == "__main__":
    # open()
    for x in range(10):
        threading.Thread(target=open).start()