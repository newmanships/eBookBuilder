import os
import glob
import shutil

path = './'
#Get total amount of chapters
list_dir = []
list_dir = os.listdir(path)
count = 0
tick = 3  #Use this against the count to write playOrder
html_list = []
html_list.append("cover")
html_list.append("copyright")

for file in list_dir:
  if file.endswith('xhtml'):
    count = count + 1
    html_list.append(file)
count = count + 2 #Compensate for cover + copyright

name = raw_input("Enter book name: ") #Eliminate spaces for UUID info

#Create toc.ncx
f = open('toc.ncx', 'w')
f.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>')
f.write('<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">')
f.write('<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">')
f.write('<head>')
f.write('<meta content="urn:uuid:' + name + '" name="dtb:uid"/>')
f.write('<meta content="2" name="dtb:depth:/>')
f.write('<meta content="0" name="dtb:totalPageCount"/>')
f.write('<meta content="0" name="dtb:maxPageNumber"/>')
f.write('</head>')
f.write('<docTitle>')
f.write('<text>' + name + '</text>')
f.write('</docTitle>')
f.write('navMap>')
f.write('<navPoint id="navPoint-1" playOrder="1">')
f.write('<navLabel><text/></navLabel>')
f.write('<content src="Text/cover.xhtml"/>')
f.write('<navPoint id="navPoint-2" playOrder="2"><navLabel>')
f.write('<text>' + name + '</text></navLabel>')
f.write('<content src="Text/copyright.xhtml"/></navPoint>')
for tick in range(2, count):
  f.write('<navPoint id="navPoint-' + str(tick) + 'playOrder="' + str(tick) + '">')
  title = html_list[tick][1:-6]
  f.write('<navLabel><text>' + title + '</text></navLabel>')
  source = html_list[tick].replace(" ", "%20")
  f.write('<content src="Text/' +  source + '"/></navPoint>')

f.write('</navPoint>')
f.write('</navMap>')
f.write('</ncx>')

f.close()

