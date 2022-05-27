#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
	docid: '97337bdc-8f1e-4b91-b444-ad54bc156c2b'
	name:
	description: >
	expirary: '->'
	version: '0.0.0.0.0.0'
	authority: document|this
	security: seclvl2
	<(WT)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||
from os.path import abspath, dirname, join
#===============================================================================||
from condor import condor
#===============================================================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#												||set path at pheonix level
#===============================================================================||

class tmplt(object):
	'''Load object that can retrieve tmplt from default tmplt store'''
	def __init__(self, path, tipe='tmplts'):
		''' '''
		self.tmplts = fonql.doc(path)

	def search(self, term, what='names'):
		'''Filter through template directories looking for search term and
		 	opening files and searching text if a text search is called'''
		if what == 'names':
			rdr = self.tmplts.read().filtr(term)
		elif what == 'text':
			rdr = self.tmplts.read()
			while True:
				terms = next(rdr, None)
				if terms == None:
					break
		return self


class mtmplt(object):
	'''Load object that can retrieve mtmplt from default tmplt store'''
	def __init__(self):
		self.mtmplts = fonql.doc(path).read()

	def search(self):
		''' '''


#==============================Source Materials=================================||
'''
''' #																			||
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
