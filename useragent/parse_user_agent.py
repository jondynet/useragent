#coding:utf-8
# Last modified: 2016-11-30 01:01:37
# by zhangdi http://jondy.net/
Mobile = {
    "Letv X500" : "乐视X500",
    "Letv X501" : "乐视X501",
    "X900+" : "乐视X900",
    "KTU84P" : "小米3",
    "Redmi 3S" : "红米3s",
    "Redmi Note 3" : "红米note3",
    "m3 note" : "小米note3",
    "Xiaomi" : "小米",
    "R7007" : "OPPOR7007",
    "OPPO R9" : "OPPOR R9",
    "R7Plusm" : "OPPOR R7",
    "OPPO R7" : "OPPOR R7",
    "OPPO A53" : "OPPOR A53",
    "Coolpad" : "Coolpad",
    "iPhone" : "iPhone",
    "vivo X7Plus" : "vivo X7Plus",
    "vivo X6Plus" : "vivo X6Plus",
    "vivo X6L" : "vivo X6L",
    "vivo X5Pro" : "vivo X5Pro",
    "vivo Y33" : "vivo Y33",
    "vivo Xplay5A" : "vivo Xplay5A",
    "GiONEE-GN9000L" : "GiONEE-GN9000L",
    "SM-N9006" : "三星N9006",
    "HUAWEI-N9006" : "华为",
  }
System = {
    "Windows NT 6.4":"Windows 10",
    "Windows NT 6.3":"Windows 8.1",
    "Windows NT 6.2":"Windows 8",
    "Windows NT 6.0":"Windows 8",
    "Windows NT 6.1":"Windows 7",
    "Windows NT 5.1":"Windows XP",
    "Macintosh": "Apple PC",
    "Android 4.2" : "Android 4.2",
    "Android 4.3" : "Android 4.3",
    "Android 4.4" : "Android 4.4",
    "Android5.0" : "Android 5.0",
    "Android 5.0" : "Android 5.0",
    "Android 5.1" : "Android 5.1",
    "Android 6.0" : "Android 6.0",
    "iPhone OS 7_1" : "iOS 7.1",
    "iPhone OS 8_0_2" : "iOS 8.0.2",
    "iPhone OS 8_1_1" : "iOS 8.1.1",
    "iPhone OS 9_2_1" : "iOS 9.2.1",
    "iPhone OS 9_3_2" : "iOS 9.3.2",
    "iPhone OS 9_3_5" : "iOS 9.3.5",
    "iPhone OS 10_1" : "iOS 10.1",
    "iPad" : "iPad",
  }
Browser = {
    "SogouMobileBrowser":"搜狗手机浏览器",
    "UCBrowser":"UC浏览器",
    "UCWEB":"UC浏览器",
    "Opera":"Opera浏览器",
    "QQBrowser":"QQ浏览器",
    "TencentTraveler":"QQ浏览器",
    "MetaSr":"搜狗浏览器",
    "360SE":"360浏览器",
    "The world":"世界之窗浏览器",
    "Maxthon":"遨游浏览器",
    "Chrome":"谷歌浏览器",
    "AppleWebKit":"Safari",
  }

def get_mobile(ua):
  for name in Mobile.keys():
    if ua.find(name) != -1:
      return Mobile[name]
  return '未知'

def get_system(ua):
  for name in System.keys():
    if ua.find(name) != -1:
      return System[name]
  return '未知'

def get_browser(ua):
  for name in Browser.keys():
    if ua.find(name) != -1:
      return Browser[name]
  return '未知'
