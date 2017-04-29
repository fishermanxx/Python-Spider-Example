# -*- coding=utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import urlparse
import re

myurl = 'http://baike.baidu.com/item/Python?sefr=cr'
response = urllib2.urlopen(myurl)
print response.getcode()
# print response.read()

html_cont = response.read()
soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')

# links = soup.find_all('a', href=re.compile(r"/item/.*?"))
# for link in links:
# 	new_url = link['href']
# 	new_full_url = urlparse.urljoin(myurl, new_url)
# 	print new_full_url

res_data = {}
title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
print u'\nTiTle: %s' % title_node.get_text()

# summary_node = soup.find('div', class_='lemma-summary').find_all('div', class_='para')
summary_node = soup.find('div', class_='lemma-summary')

fileName = 'text.txt'
f = open(fileName, 'wb')
# for param in summary_node:
# 	f.write(param.get_text().encode('utf-8'))
# 	print 'save successfully!'

f.write(summary_node.get_text().encode('utf-8'))
f.close()


