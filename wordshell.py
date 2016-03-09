import urllib
import sys
import re
import json
import os
from pyquery import PyQuery as pq

eg = False

flag_detail = False

read_word = True

if __name__ == '__main__':
	words = []
	try:
		file = open('wordshell.words.json', 'r')
		words = json.loads(file.read())
	except Exception, e:
		pass
	else:
		file.close()
	finally:
		pass
#		file.close()
	while True:
		word = raw_input('>> ')
		is_in = False
		for iw in words:
			#print words[iw][0]
			print iw

		if word in words:
			words[ words.index(word) ]['times'] += 1
		else:
			words.append( {word: {u'times': 1}} )
			#words[-1]['times'] = 1
		file = open('wordshell.words.json', 'w')
		try:
			file.write(json.dumps(words))
		finally:
			file.close()
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

		if read_word:
			audio = urllib.urlopen('http://dict.youdao.com/dictvoice?audio=' + urllib.quote(word))
			audiofn = os.path.expandvars('$TMPDIR/') + urllib.quote(word)
			audiofp = open(audiofn, 'wb')
			audiofp.write(audio.read())
			audiofp.close()
			os.system('afplay ' + audiofn)

		#if eg:
		#    origs=re.findall(r'<orig>(?P<orig>.*?)</orig>', xmls, re.M|re.I|re.S|re.U)
		#    trans=re.findall(r'<trans>(?P<trans>.*?)</trans>', xmls, re.M|re.I|re.S|re.U)
		#    for i in range(len(origs)):
		#		print "%d. %s"%(i+1,origs[i])
		#		print "%s  %s"%(' '*((i+1)/10+1),trans[i])


