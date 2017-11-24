# -*- coding:utf-8 -*-
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
'''
zuozhe_pattern=re.compile('<p class="user_name_list">.*?<a.*?>(.*?)</a>',re.S)
zuozhe_list=re.findall(zuozhe_pattern,html)
for item in zuozhe_list:
    print item

biaoti_pattern=re.compile('<h1 class="dp-b">.*?<a.*?>(.*?)</a>',re.S)
biaoti_list=re.findall(biaoti_pattern,html)
for item in biaoti_list:
    print item


conten_pattern=re.compile('<h1 class="dp-b">.*?<div class="content-img clearfix pt10 relative">(.*?)</div>',re.S)
conten_list=re.findall(conten_pattern,html)
for item in conten_list:
    print item



dianzanshu_pattern=re.compile('<span class="fl ding">.*?<em>(.*?)</em>',re.S)
dianzanshu_list=re.findall(dianzanshu_pattern,html)
for item in dianzanshu_list:
    print item
'''

all_pattern = re.compile('<p class="user_name_list">.*?<a.*?>(.*?)</a>.*?<h1 class="dp-b">.*?<a.*?>(.*?)</a>.*?<div class="content-img clearfix pt10 relative">(.*?)</div>.*?<span class="fl ding">.*?<em>(.*?)</em>',re.S)
all_list = re.findall(all_pattern, html)
for item in all_list:
    print "name:" + item[0]
    print "title:" + item[1]
    print "content:" + item[2].strip()
    print "good:" + item[3]
    print "-----------------"






