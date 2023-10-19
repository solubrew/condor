#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(meta)>:
	DOCid: <^[uuid]^>
	Name:
	description: >
	expirary: <[expiration]>
	Version: <[Version]>
	path: <[LEXIvrs]>panda/LEXI/
	outline: <[outline]>
	authority: document|this
	security: seclvl2
	<(wt)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||
from os.path import abspath, dirname, join
#===============================================================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#												||set path at pheonix level
version = '0.0.0.0.0.0'#												||
wolfpack = '{0}wolf/pack/bash'.format(there)
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
#================================:::DNA:::======================================||
''' #																			||
dna: #																			||
<@[datetime]@>: #																||
	<[class]>: #																||
		version: <[active:.version]> #											||
		test: #																	||
		description: > #														||
			<[description]> #													||
		work: #																	||
			- <@[work_datetime]@> #												||
<[datetime]>: #																	||
	here: #																		||
		version: <[active:.version]> #											||
		test: #																	||
		description: > #														||
			<[description]> #													||
		work: #																	||
			- <@[work_datetime]@> #												||
''' #																			||
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
