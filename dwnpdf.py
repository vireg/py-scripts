# Script to automatically download from links to PDFs on a page
# All links to PDFs are of the form url+fileName.pdf

import urllib.request
from bs4 import BeautifulSoup
import re

url =  "http://pages.cs.wisc.edu/~remzi/OSTEP/"	#raw_input('Enter - ')
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "lxml")

# Retrieve all of the anchor tags
tags = soup('a')

# Gather and store all ".pdf" links in a list
lst = []
for tag in tags:
	link = tag.get('href', None)
	x = re.findall(".pdf", str(link))
	if x!=[]:
		print(link)
		lst.append(str(link))

# Download
for fileName in lst:
	try:
		dlink = url+fileName
		u = urllib.request.urlopen(dlink)
		meta = u.info()
		#print(meta)
		if "Content-Length" in meta:
			fileSize = int(meta["Content-Length"])
			print("Downloading: %s Bytes: %s" % (fileName, fileSize))
		f = open(fileName, 'wb')
		f.write(u.read())
		f.close()
	except urllib.error.HTTPError as err:
		if err.code == 404:
			print("Error 404: ",dlink)

# downloadedSize = 0
# if "Content-Length" in meta:
	# fileSize = int(meta["Content-Length"])
	# print("Downloading: %s Bytes: %s" % (fileName, fileSize))
	# blockSize = 8192
	# while True:
		# buffer = u.read(blockSize)
		# if not buffer:
			# break
		# downloadedSize += len(buffer)
		# f.write(buffer)
		# status = r"%10d  [%3.2f%%]" % (downloadedSize, downloadedSize * 100 / fileSize)
		# #status = status + chr(8)*(len(status)+1)
		# print(status)
# else:
	# print("Downloading: unknown bytes...")
	# f.write(u.read())

# f.close()