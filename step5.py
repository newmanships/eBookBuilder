import os
import shutil
import glob

path = './'
list_dir = []
list_dir = os.listdir(path)
count = 0
html_list = []
foldernames = ""

source = '/book/OEBPS/Text' # This is directory format for eBooks.  Change to correct source for your computer but keep these last 3 folders
if not os.path.exists(source):
  os.makedirs(source)

for path, subdirs, files in os.walk(path):
  if subdirs:
    html_list.append(subdirs)

chapters = raw_input("Enter the number of chapters: ") #Hack to get around lists

for file in list_dir:
  if file.endswith('xhtml'):
    count = count + 1
    shutil.copy(file, source)

src = '/logo.jpg' #Enter correct source for your logo
dst = '/book/OEBPS/Images' #Ensure correct destination but include these last 3 folders

if not os.path.exists(dst):
  os.makedirs(dst)
shutil.copy(src, dst)

src2 = '/eBook-files/mimetype' #Again set to correct dir but include these last 2 folders
dst2 = '/book' #Same as above, keep this folders

shutil.copy(src2, dst2)

src3 = '/eBook-files/META-INF/container.xml' #Again, keep this part and modify for your computer
dst3 = '/book/META-INF' #You know the drill...

if not os.path.exists(dst3):
  os.makedirs(dst3)

shutil.copy(src3, dst3)

src4 = '/eBook-files/zconclusion.xhtml' #Again... also ensure this is name of your conclusion file
dst4 = '/book/OEBPS/Text' # Again...

if not os.path.exists(dst4):
  os.makedirs(dst4)

shutil.copy(src4, dst4)

x = 1
while x <= int(chapters):
  
  src5 = '/' + str(x) # Yet another one to set
  dst5 = '/book/OEBPS/Images/' + str(x) # And this one

  if not os.path.exists(dst5):
    os.makedirs(dst5)
  for item in os.listdir(src5):
    s = os.path.join(src5, item)
    d = os.path.join(dst5, item)
    if os.path.isdir(s):
      shutil.copytree(s, d, symlinks, ignore)
    else:
      shutil.copy2(s, d)
  x = x+1

src6 = '/script/content.opf' #Make sure this is whatever directory the content.opf was created in
dst6 = '/book/OEBPS' #Set this one too

if not os.path.exists(dst6):
  os.makedirs(dst6)

shutil.copy(src6, dst6)

src7 = '/script/toc.ncx' #Same as the content.opf
dst7 = '/book/OEBPS' #Almost done

shutil.copy(src7, dst7)

cover = raw_input("Enter the cover name (including file extension: ")
src8 = '/script/' + cover  # This is set to where your cover image is
dst8 = '/book/OEBPS/Images' #Last one!!!
shutil.copy(src8, dst8)


