#coding:utf-8
# Last modified: 2016-05-16 17:05:03
# by zhangdi http://jondy.net/

System = {
    "Windows NT 6.4":"Windows 10",
    "Windows NT 6.3":"Windows 8.1",
    "Windows NT 6.2":"Windows 8",
    "Windows NT 6.0":"Windows 8",
    "Windows NT 6.1":"Windows 7",
    "Windows NT 5.1":"Windows XP",
    "Macintosh": "Apple PC",
    "Android" : "Android",
    "iPhone" : "iPhone",
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

def get_system(ua):
  for name in System:
    if ua.find(name) != -1:
      return System[name]
  return '未知'

def get_browser(ua):
  for name in Browser:
    if ua.find(name) != -1:
      return Browser[name]
  return '未知'
