import urllib
import sys
import re
from pyquery import PyQuery as pq

eg = False

flag_detail = False

if __name__ == '__main__':
	while True:
		word = raw_input('>> ')
		#t = pq( urllib.urlopen('http://dict.cn/' + urllib.quote(word)).read().decode('utf-8') )
		t = pq(url = 'http://dict.cn/' + urllib.quote(word))
		basic = t('ul.dict-basic-ul:first')
		for i in basic.children():
			li = pq(i)
			if ('search_in_n' in li.html()):
				continue
			print '   ' + li.text()

		if flag_detail:
			detail = t('div.layout-detail:first')
			print detail.html()
			for i in detail.children():
				e = pq(i)
				print e.text()

		#if eg:
        #    origs=re.findall(r'<orig>(?P<orig>.*?)</orig>', xmls, re.M|re.I|re.S|re.U)
        #    trans=re.findall(r'<trans>(?P<trans>.*?)</trans>', xmls, re.M|re.I|re.S|re.U)
        #    for i in range(len(origs)):
        #        print "%d. %s"%(i+1,origs[i])
        #        print "%s  %s"%(' '*((i+1)/10+1),trans[i])
