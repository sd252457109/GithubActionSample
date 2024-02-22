import os
import requests

cookie = os.environ.get("JD_COOKIE")

url = ("https://api.m.jd.com/client.action?functionId=hours_home_Tag&clientVersion=12.4.0&build=99084&client=android&partner=huawei&oaid=ffbfcefe-fffe-c980-dfff-e73eddf74bdc&sdkVersion=26&lang=zh_CN&harmonyOs=0&networkType=wifi&uemps=0-2-0&ext=%7B%22prstate%22%3A%220%22%2C%22pvcStu%22%3A%221%22%2C%22cfgExt%22%3A%22%7B%5C%22privacyOffline%5C%22%3A%5C%220%5C%22%7D%22%7D&eid=eidA86b78120d7s6U8Kdmb4cTmSkUA0KWUFYS1PCnyeMZda5iBo5Jp0N71%2FS07Om0xb4Dk5Jt2hCf%2FOHN8DqS1vJOWbJ3srw%2Fm0oDVKYj%2FBxmngdMRVh&x-api-eid-token=jdd01YQJX6KVPDDC5EXHLGU2LKI4VCXR6WGMHE3SXWFXMDFDTMTVYJQL3TKSNG6JPJHXTB45BDU3BGTAMUUVPEYQ6Z3AGB2G7YCFLDQT5MMI01234567&ef=1&ep=%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1708563001633%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22area%22%3A%22CJDpCJKzCv8yENuyDV81DzqzEG%3D%3D%22%2C%22d_model%22%3A%22UPTLBUPCCNK%3D%22%2C%22wifiBssid%22%3A%22YJPrYwVrYtDwC2SnCwVuDNrwZtG0ZwO5CtY1CJq1Y2C%3D%22%2C%22osVersion%22%3A%22EM4mBtK%3D%22%2C%22d_brand%22%3A%22IPVLV0VT%22%2C%22screen%22%3A%22CJO5Dse3CtK%3D%22%2C%22uuid%22%3A%22YtG5YwU1EJcmENczDQY3ZG%3D%3D%22%2C%22aid%22%3A%22YtG5YwU1EJcmENczDQY3ZG%3D%3D%22%2C%22openudid%22%3A%22YtG5YwU1EJcmENczDQY3ZG%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D&st=1708563004766&sign=67c499a5697642da419b9564ee8a512d&sv=110")

headers = {"Connection": 'keep-alive',
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "Cache-Control": 'no-cache',
           "User-Agent": "okhttp/3.12.1;jdmall;android;version/10.3.4;build/92451;",
           "accept": "*/*",
           "connection": "Keep-Alive",
           "Accept-Encoding": "gzip,deflate",
           "Cookie": cookie
           }

response = requests.post(url=url, headers=headers)
print(response.text)
