'''
	Downloading Script
'''
from urllib.request import urlopen
import re
import sys
from os.path import join
#import the beautiful soup library
from bs4 import BeautifulSoup
count = 0

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
	save1 = open(join("./parks/",filename),'w')
	save1.write(text)
	save1.close()

def crawler(lines,limit):
	global count
	final = []
	for i in range(0,len(lines)):
		url = str(lines[i])
		try:
			download(url)			
			count = count+1
			print(count)
			final.append(url)
		except Exception as e:
			print(e)
		if (count+1) == (limit+1):
			break
	finallinks = open(join("./parks/","finallinks.txt"),'w')
	for f in final:
		finallinks.write(f+"\n")


def main():
	linkfile = open("./parks/links.txt","r")
	# print(linkfile.read())
	line1 =[line.strip('\n') for line in open("./parks/links.txt","r")]
	lines = [line2 for line2 in line1 if not line2.endswith('.jpg') and not '#' in line2]
	refinedlinks = open(join("./parks/","refinedlinks.txt"),'w')

	for r in lines:
		refinedlinks.write(r+"\n")

	print("The number of lines before removal:")
	print(len(line1))
	#print(lines)
	print("The number of lines after removal:")
	print(len(lines))
	crawler(lines,int(sys.argv[1]))

main()



