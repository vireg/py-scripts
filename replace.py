# Script to find print statements in file and replace with print() in-place
import fileinput
import re

for line in fileinput.input("www-coursera-downloader.py", inplace = True):
	x = re.findall("print ", line)
	if x!=[]:
		strng = re.sub("print ", "print(", line)
		strng = strng.strip("\n")
		strng = strng+")"
		print (strng)
	else:
		print(line.strip("\n"))	# strip because print() automatically adds "\n"