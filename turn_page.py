#https://github.com/xiaocong/uiautomator
from uiautomator import device as d
d.dump("hierarchy.xml")

import time
import datetime
import random

#d = Device('014E05DE0F02000E', adb_server_host='192.168.1.68', adb_server_port=5037)



def auto_read():
    #from uiautomator import device as d
    #d.screen.on()
    import uiautomator2 as u2
    d = u2.connect()
    d.swipe(500, 100 * random.uniform(3, 5), 500, 100)
    if d(text="展开全文").exists:
       d(text='展开全文').click()


def home():
    d.press.home()
    #d.press.back()
    #d.press("back")
    #d.press(0x07, 0x02)

def lock():
    d.freeze_rotation()
def unlock():
    d.freeze_rotation(False)
def shot():
    d.screenshot("home.png")
def position():
    info=d.info
    #print(info)
#{'currentPackageName': 'com.tencent.weread', 'displayHeight': 2016, 'displayRotation': 0, 'displaySizeDpX': 360, 'displaySizeDpY': 720, 'displayWidth': 1080, 'productName': 'lineage_chiron', 'screenOn': True, 'sdkInt': 27, 'naturalOrientation': True}
#[1070, 2006]
    w=info['displayWidth']
    h=info['displayHeight']
    r=info['displayRotation']
    return [i-10 for i in (w,h)]

def sleep1():
    t=random.randint(45,50)
    time.sleep(t)

def turn_page(p):
    w,h=p
    d.click(w,h)
    #d.long_click(x, y)
    #d.swipe(1000, 500, 30, 500)
    #d.drag(sx, sy, ex, ey)
    #d.drag(sx, sy, ex, ey, steps=10)


def light():
    d.wakeup()
    d.screen.on()

def main():
    light()
    i=0
    while True:
        i=i+1
        print(i)
        turn_page(position())
        sleep1()

main()




