# -*- coding: utf-8 -*-
import requests
import time
import re

class Tool():
	def replace(self, x):
		x = re.sub(re.compile('<br>|</br>|<br/>'), "", x)
		return x.strip()

class Spider(object):

	#初始化
	def __init__(self):
		self.siteURL = 'http://www.qiushibaike.com/'
		self.tool=Tool()

	#获取网页源码
	def getSource(self, url):
		user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
		headers = {'User_agent':user_agent}
		r = requests.get(url, headers=headers)
		# print r.url
		# print r.text
		return r.text

	def getDetailPage(self, detailURL):
		source = self.getSource(detailURL)

		# pattern=re.compile('<div class="author.*?<h2>(.*?)</h2>.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span.*?stats-vote.*?number">(.*?)</i>.*?stats-comments.*?number">(.*?)</i>.*?up.*?number hidden">(.*?)</span>.*?down.*?number hidden">(.*?)</span>',re.S)
		pattern=re.compile('<div class="author.*?<h2>(.*?)</h2>.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?number">(.*?)</i>',re.S)
		items = re.findall(pattern, source)

		return items

	#保存信息写入文件
	def saveDetailPage(self, data, name):
		fileName = 'page'+name+'.txt'
		f = open(fileName, 'wb')

		number = 1
		for item in data:
			content = self.tool.replace(item[2])
			# print number, u'楼', u'\n楼主：', item[0], u'', item[1], u'岁',\
			# u'\n发言:', content, u'\nvote:', item[3]
			number+=1
			f.write("\n%s floor, \n author: %s, \ncontent: %s \n" % (number, item[0].encode("gbk"), content.encode("gbk")) )

		print 'save page%s successfully!' % name
		f.close()

	def OnePage(self, detailURL, name):
		data = self.getDetailPage(detailURL)
		self.saveDetailPage(data, str(name))

	def getAllPage(self, start, end):
		if start == 1:
			print u'正在获取第1页的数据...'
			detailURL = self.siteURL
			self.OnePage(detailURL, start)
			number = 2
			for page in range(2, end+1):
				print u'正在获取第',number,u'页的数据'
				detailURL = self.siteURL + '8hr/page/' + str(page) + '/?s=4964625'
				self.OnePage(detailURL, number)
				time.sleep(2)
				number += 1
			if number == end+1:
				print u'', u'\n加载结束！'
				return False
		elif start>1:
			number=start
			for page in range(2, end+1):
				print u'正在获取第',number,u'页的数据'
				detailURL = self.siteURL + '8hr/page/' + str(page) + '/?s=4964625'
				self.OnePage(detailURL, number)
				time.sleep(2)
				number += 1
			if number == end+1:
				print u'', u'\n加载结束！'
				return False			

spider = Spider()
# spider.getSource(spider.siteURL)
# data = spider.OnePage(spider.siteURL, 1)
start_x = u'请输入起始页: '.encode('gbk')
end_x = u'请输入结束页: '.encode('gbk')
# spider.getAllPage(start=int(raw_input('start:')), end=int(raw_input('end:')))
spider.getAllPage(start=int(raw_input(start_x)), end=int(raw_input(end_x)))





