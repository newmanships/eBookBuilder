import os
import glob
import shutil

path = './'
listing = os.listdir(path)

name = raw_input("Enter a name: ")
chapter = raw_input("Enter chapter: ") #To keep track of images for order
#Add chapter to filename to keep track of order for contents
filename = chapter + name + '.xhtml'

def build_chapter(name, chapter, filename	):
  FILE = open(filename,'w')
  FILE.write('<?xml version="1.0" encoding="utf-8" standalone="no"?>')
  FILE.write('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">')
  FILE.write('<html xmlns="http://www.w3.org/1999/xhtml">')
  FILE.write('<head>')
  FILE.write('<title>' + name + '</title>')
  FILE.write('<style type="text/css">')
  FILE.write('body {background: #000; color: #fff;text-align: center;}')
  FILE.write('img {margin: 0 auto; text-align: center;}')
  FILE.write(' p.sgc-1 {text-align: center;}')
  FILE.write('</style>')
  FILE.write('</head>')
  FILE.write('<body>')
  FILE.write('<h1 id="heading_id_2">' + name + '</h1>')
  for infile in listing:
     if infile[-3:].lower() == 'jpg':
	  FILE.write( '<p>&nbsp;<img src="../Images/' + chapter + '/' +  infile + '"/></p>') #Set to correct directory

  FILE.write('</body>')
  FILE.write('</html>')

  FILE.close()
  ensure_dir(chapter)
  move_files(chapter, listing)

#Create folder based on chapter number
def ensure_dir(chapter):
  if os.path.exists(chapter):
    chapter = raw_input("Chapter already exists, please choose another: ")
  os.makedirs(chapter)
  return

#Move images into individual chapter folders
def move_files(chapter, listing):
  src = '/' #Enter your source directory listing here
  dst = '/' + chapter + '/' #Enter your destination directory here
  for infile in listing:
    if infile[-3:].lower() == 'jpg':
      shutil.move(infile, dst)

if __name__=="__main__":
  build_chapter(name, chapter, filename)
