from urllib.request import urlopen
import re
from os.path import join
#import the beautiful soup library
from bs4 import BeautifulSoup

def download(url):
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

linkfile = open("./crawled/links.txt","r")
# print(linkfile.read())

lines =[line.strip('\n') for line in open("./crawled/links.txt","r")]
print("The number of lines :")
print(len(lines))
count = 1
for i in range(0,len(lines)):
	url = str(lines[i])
	try:
		print(count)
		download(url)
		count = count+1
	except Exception as e:
		print(e)


