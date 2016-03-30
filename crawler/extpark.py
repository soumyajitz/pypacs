# No longer urllib is available
'''
	Extraction Script
'''
from urllib.request import urlopen
import re
from os.path import join
#import the beautiful soup library for HTML parsing
from bs4 import BeautifulSoup
'''
Python scraping url used as an example
'''
try:
	html1 = urlopen("https://en.wikipedia.org/wiki/Motorcycle")
except HTTPError as e:
	print(e)
if html1 is None:
	print("URL is not found")
else:
	bsObj = BeautifulSoup(html1.read(),"html.parser")
	html1.close()
	#print(bsObj.html.text)

	allText = bsObj.html
	allText = str(allText)
	#print(bodyText.strip())
	# print(allText)
	list1 = re.findall(r'href=[\'"]?([^\'" >]+)',allText)
	#print(', '.join(""+list1))
	list2 = []
	src = str(list1[11])
	for l in list1[15:]:
		if l.startswith('http'):
			list2.append(l)
		else:
			list2.append("https://en.wikipedia.org"+l)
crawledlinks = open(join("./parks/","links.txt"),'w')
for k in list2:
	print(k)
	crawledlinks.write(k+"\n")
url1 = str(list2[10])
print(url1)


# try:
# 	resp1 = urlopen(url1)
# except HTTPError as e:
# 	print(e)
# bsObj1 = BeautifulSoup(resp1.read(),"html.parser")
# f = open('url1'+'.html', 'w')
# f.write(bsObj1)
# resp1.close()

