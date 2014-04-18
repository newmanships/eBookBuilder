import os


name = raw_input("Enter book name: ")
cover = raw_input("Enter file name (including extension) of cover: ")

#Create cover.xhtml

f = open("cover.xhtml", "w")
intro =('<?xml version="1.0" encoding="utf-8" standalone="no"?>')
intro2 = ('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">')
f.write(intro)
f.write(intro2)
f.write('<html xmlns="http://www.w3.org/1999/xhtml">')
f.write('<head><title>' + name + '</title><style type="text/css">')
#CSS data
f.write('body {background: #000; color: #fff;text-align: center;}')
f.write('img {margin: 0 auto; text-align: center;}')
f.write('p.sgc-1 {text-align: center;}')
f.write('span.sgc-2 {font-weight: normal; font-size: medium;}')

f.write('</style></head><body>')
f.write('<h1 id="heading_id_2"><span class="sgc-2"><img alt="" src="../Images/' + cover + '" /><br /></span></h1></body></html>')

f.close()
#Create copyright.xhtml 
g = open("copyright.xhtml", "w")
g.write(intro)
g.write(intro2)
g.write('<html xmlns="http://www.w3.org/1999/xhtml">')
g.write('<head><title>' + name + '</title><style type="text/css">')
#CSS data
g.write('body {background: #000; color: #fff;text-align: center;}')
g.write('img {margin: 0 auto; text-align: center;}')
g.write('p.sgc-1 {text-align: center;}')
g.write('</style></head><body>')
g.write('<h2 class="sgc-2 sgc-1 sgc-2" id="heading_id_2">' + name + '</h2>')
g.write('<div class="sgc-3"><img alt="" src="../Images/logo.jpg" /><br /></div>')
# On the above line make sure the src == what your logo file is named.  The 2 lines below change to your website/company name + any text you would like to add.
g.write('<p class="sgc-2 sgc-2 sgc-2 sgc-1 sgc-2 sgc-3 sgc-2">Visit <a href="http://YourWebsite.com">YourWebsite.com</a> today!</p>')
g.write('<p class="sgc-2 sgc-2 sgc-3 sgc-1 sgc-2 sgc-3 sgc-2"><br /></p>')
g.write('<p class="sgc-2 sgc-3 sgc-1 sgc-2 sgc-3 sgc-2"><small>Copyright <a href="http://YourWebsite.com">YourWebsite.com</a>.<br>All Rights Reserved.</small></p>')
g.write('</body></html>')

g.close()
