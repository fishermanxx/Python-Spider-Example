from bs4 import BeautifulSoup


html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
""" 

soup = BeautifulSoup(html, "lxml")
print soup.prettify()

print '===================================================================================='
print soup.title
print soup.head
print soup.a
print soup.p
print '===================================================================================='
print soup.name
print soup.head.name
print soup.p.attrs
print soup.p.string
print '===================================================================================='
# print soup.head.contents
print soup.body.contents
