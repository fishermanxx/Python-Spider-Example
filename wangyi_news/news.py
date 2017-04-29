# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import requests
import re
from lxml import etree


def Spider(url):
	i = 0
	print "downloading ", url
	myPage = requests.get(url).content.decode("gbk")
	# myPage = urllib2.urlopen(url).read().decode("gbk")
	# print myPage

	myPageResults = Page_Info(myPage)
	# print myPageResults

	save_path = u"wangyinews"
	filename = str(i)+"_"+u"news_rank"
	StringListSave(save_path, filename, myPageResults)

	i += 1
	for item, url in myPageResults:
		print "dowloading ", url
		new_page = requests.get(url).content.decode("gbk")

		newPageResults = New_Page_Info(new_page)
		filename = str(i)+"_"+item
		StringListSave(save_path, filename, newPageResults)
		i += 1



def Page_Info(myPage):
	'''Regex'''
	##<div class="titleBar" id="whole"><h2>全站</h2><div class="more"><a href="http://news.163.com/special/0001386F/rank_whole.html">更多</a></div></div>
	mypage_Info = re.findall(r'<div class="titleBar" id=".*?"><h2>(.*?)</h2><div class="more"><a href="(.*?)">.*?</a></div></div>', myPage, re.S)
	return mypage_Info


def StringListSave(save_path, filename, slist):
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	path = save_path+"/"+filename+".txt"
	with open(path, "w+") as fp:
		for s in slist:
			fp.write("%s\t\t%s\n" % (s[0].encode("utf8"), s[1].encode("utf8")))


def New_Page_Info(new_page):
	'''Regex(slow) or Xpath(fast)'''
	##<td class="red"><span>1</span><a href="http://sports.163.com/17/0320/10/CFVBLEGE0005877U.html">说一不二!LBJ命小弟为勒夫让座 菜鸟只能坐地上</a></td>
	new_page_Info = re.findall(r'<td class=".*?">.*?<a href="(.*?)">(.*?)</a></td>', new_page, re.S)

	results = []
	for url, item in new_page_Info:
		results.append((item, url))

	return results

 #    dom = etree.HTML(new_page)
 #    new_items = dom.xpath('//tr/td/a/text()')
 #    new_urls = dom.xpath('//tr/td/a/@href')
 #    assert(len(new_items) == len(new_urls))
	# return zip(new_items, new_urls)



if __name__ == '__main__':
	print "start"
	start_url = "http://news.163.com/rank/"
	Spider(start_url)
	print "end"