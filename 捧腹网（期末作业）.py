# -*- coding:utf-8 -*-
#捧腹网爬虫
import urllib
import urllib2
import re



user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
 
page = 1
url = 'https://www.pengfu.com/index_' + str(page) + '.html'

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    html = response.read().decode('utf-8')
except urllib2.URLError, e:
    if hasattr(e,"code"):

        
        print e.code
        
    if hasattr(e,"reason"):
        
        print e.reason

all_pattern = re.compile('<p class="user_name_list">.*?<a.*?>(.*?)</a>.*?<h1 class="dp-b">.*?<a.*?>(.*?)</a>.*?<div class="content-img clearfix pt10 relative">(.*?)</div>.*?<span class="fl ding">.*?<em>(.*?)</em>',re.S)
all_list = re.findall(all_pattern, html)
for item in all_list:
    print "name:" + item[0]
    print "title:" + item[1]
    print "content:" + item[2].strip()
    print "good:" + item[3]
    print "-----------------"

    input = raw_input()
    if input == "":
        print "nextPage:"
        continue
    elif input =="Q":
        break






