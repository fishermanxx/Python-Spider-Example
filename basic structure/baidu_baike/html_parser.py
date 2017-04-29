# -*- coding=utf-8 -*-
from bs4 import BeautifulSoup
import urlparse
import re

class HtmlParser(object):

	# <a target="_blank" href="/item/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6">
	def _get_new_urls(self, url, soup):
		new_urls = set()
		links = soup.find_all('a', href=re.compile(r"/item/.*?"))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(url, new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self, url, soup):
		res_data = {}

		res_data['url'] = url

		# <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>.*?</dd>
		title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
		res_data['title'] = title_node.get_text()

		# <div class="lemma-summary" label-module="lemmaSummary">
		# <div class="para" label-module="para">(.*?)</div>
		# </div>
		summary_node = soup.find('div', class_='lemma-summary')
		res_data['summary'] = summary_node.get_text()

		return res_data

	def parse(self, url, html_cont):
		if url is None or html_cont is None:
			return 

		soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
		new_urls = self._get_new_urls(url, soup)
		new_data = self._get_new_data(url, soup)
		return new_urls, new_data