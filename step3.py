import os
import glob
import shutil
import fnmatch

path = './'
#Get total amount of chapters/image folders
list_dir = []
list_dir = os.listdir(path)
count = 0
id_count = 1  #Use this to fill in id field w/ unique identifier each time
html_list = []
html_order = [] #For keeping idref in spine in order
x_var = 0 #Use to iterate since I can't use for apparently

for file in list_dir:
  if file.endswith('xhtml'):
    count = count + 1
    html_list.append(file) #Use later to list in manifest

#Get all images in subdirectories
matches = []
true_match = [] #Correct path name starting w/ Images/
for path, subdirs, files in os.walk(path):
  for filename in fnmatch.filter(files, '*.jpg'):
    matches.append(os.path.join(path, filename))
  
    image = matches[x_var][1:]
    true_match.append('Images' + image)
    x_var = x_var + 1

name = raw_input("Enter book name (Must match exactly as step 2!): ") #Eliminate spaces for UUID info
author = raw_input("Enter Author's Name: ")
cover = raw_input("Enter cover name (including file extension): ")

f = open("content.opf", "w")
f.write('<?xml version="1.0" encoding="utf-8" standalone="yes"?>')
f.write('<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="2.0">')
f.write('<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">')
f.write('<dc:identifier id="BookId" opf:scheme="UUID">urn:' + name + '</dc:identifier>')
f.write('<dc:title>' + name + '</dc:title>')
f.write('<dc:creator opf:role="aut">' + author + '</dc:creator>')
f.write('<dc:language>en</dc:language>')
f.write('<meta name="cover" content="' + cover + '" />')
f.write('</metadata>')

f.write('<manifest>')
f.write('<item href="toc.ncx" id="ncx" media-type="application/x-dtbncx+xml" />')
for y in true_match:
  f.write('<item href="' + y + '" id="' + 'aa' + str(id_count) + '" media-type="image/jpeg" />')
  id_count = id_count + 1
for x in html_list:
  source = x.replace(" ", "%20")
  source2 = source.replace("%20", "_")
  f.write('<item href="Text/' + source + '" id="' + source2[1:] + '" media-type="application/xhtml+xml" />')
  id_count = id_count + 1
  html_order.append(source)

#Make sure your logos, conclusion, copyright & covers match the below names.
f.write('<item href="Images/logo.jpg" id="logo.jpg" media-type="image/jpeg" />')
f.write('<item href="Text/zconclusion.xhtml" id="zconclusion.xhtml" media-type="application/xhtml+xml" />')
f.write('<item href="Text/copyright.xhtml" id="copyright.xhtml" media-type="application/xhtml+xml" />')
f.write('<item href="Text/cover.xhtml" id="cover.xhtml" media-type="application/xhtml+xml" />')
f.write('<item href="Images/' + cover + '" id="cover" media-type="image/jpeg" />')
f.write('</manifest>')
f.write('<spine toc="ncx">')
f.write('<itemref idref="cover.xhtml" />')
f.write('<itemref idref="copyright.xhtml" />')
for z in html_order:
  f.write('<itemref idref="' + z + '" />')
f.write('<itemref idref="zconclusion.xhtml" />')
f.write('</spine>')
f.write('<guide>')
f.write('<reference href="Text/cover.xhtml" title="Cover" type="cover" />')
f.write('</guide></package>')

