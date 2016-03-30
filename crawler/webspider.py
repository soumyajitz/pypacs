from urllib.request import urlopen
import re
from os.path import join
#import the beautiful soup library
from bs4 import BeautifulSoup

linkfile = open("./crawled/links.txt","r")
# print(linkfile.read())

lines =[line.strip('\n') for line in open("./crawled/links.txt","r")]
print(lines[10])

url = str(lines[27])
try:
	html1 = urlopen(url)
except HTTPError as e:
	print(e)
if html1 is None:
	print("URL is not found")
else:
	textObj = BeautifulSoup(html1.read(),"html.parser")
	html1.close()
	title = str(textObj.title)
	title = re.sub('<[^>]*>', '', title)
	print(title)
	text = str(textObj.html)
	#print(text)
	path = str(url[8:])
	print(path)
	filename = str(title+".htm")
save1 = open(join("./crawled/",filename),'w')
save1.write(text)
save1.close()