# python spider version 2.7.1
import urllib2

url = "http://www.baidu.com"
response=urllib2.urlopen(url)
print response.read