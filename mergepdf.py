# Script to merge all PDF files in the current working directory

import PyPDF2
import os
import re

mergedFile = input('Enter name of output PDF file: ')

# Take all PDF files in the current folder
files = os.listdir('.')					# list of filename strings for each file in the current working directory
lst=[]
for file in files:
	x = re.findall("\.pdf", file)
	if x!=[]:
		print(file)
		lst.append(file)

# Open all PDF files in read mode
fileList=[]
for pdf in lst:
	pdfFileObj = open(pdf, 'rb')
	fileList.append(pdfFileObj)

# Create PdfFileReader objects from PDF file list
readerList=[]
for pdfFile in fileList:
	pdfReader = PyPDF2.PdfFileReader(pdfFile)
	readerList.append(pdfReader)

totalPages = 0	
for pr in readerList:
	print(pr.numPages)
	totalPages += pr.numPages
print("total pages:",totalPages)

# combine read PDF files
pdfWriter = PyPDF2.PdfFileWriter()
for pr in readerList:
	for pageNum in range(pr.numPages):
		pageObj = pr.getPage(pageNum)
		pdfWriter.addPage(pageObj)

# write to a new PDF file
if os.path.isfile(mergedFile+".pdf"):
	print('File already exists, specify another filename')
else:
	pdfOutputFile = open(mergedFile+".pdf", 'wb')
	pdfWriter.write(pdfOutputFile)
	pdfOutputFile.close()

# Close all read files
for pdfFile in fileList:
	pdfFile.close()