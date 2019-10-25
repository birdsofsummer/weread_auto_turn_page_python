import uiautomator2 as u2
# https://github.com/openatx/uiautomator2


def conn():
    d = u2.connect('10.0.0.1') # alias for u2.connect_wifi('10.0.0.1')
    print(d.info)
#"am start -n com.tencent.weread/com.tencent.weread.ReaderFragmentActivity"


def init():
    pack="com.tencent.weread"
    act="com.tencent.weread.ReaderFragmentActivity"
    pa="/".join([pack,act])
    d.app_start(pa)
