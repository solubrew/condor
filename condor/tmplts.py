#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<<<<<<< HEAD
<(META)>:
	docid: '97337bdc-8f1e-4b91-b444-ad54bc156c2b'
	name:
	description: >
	expirary: '->'
	version: '0.0.0.0.0.0'
	authority: document|this
	security: seclvl2
	<(WT)>: -32
=======
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
>>>>>>> master
'''
# -*- coding: utf-8 -*-
#===============================================================================||
from os.path import abspath, dirname, join
#===============================================================================||
<<<<<<< HEAD
=======

#===============================================================================||
>>>>>>> master
from condor import condor
#===============================================================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#												||set path at pheonix level
<<<<<<< HEAD
#===============================================================================||

=======
version = '0.0.0.0.0.0'#												||
wolfpack = '{0}wolf/pack/bash'.format(there)
#===============================================================================||


>>>>>>> master
class tmplt(object):
	'''Load object that can retrieve tmplt from default tmplt store'''
	def __init__(self, path, tipe='tmplts'):
		''' '''
		self.tmplts = fonql.doc(path)
<<<<<<< HEAD

=======
>>>>>>> master
	def search(self, term, what='names'):
		'''Filter through template directories looking for search term and
		 	opening files and searching text if a text search is called'''
		if what == 'names':
			rdr = self.tmplts.read().filtr(term)
<<<<<<< HEAD
=======

>>>>>>> master
		elif what == 'text':
			rdr = self.tmplts.read()
			while True:
				terms = next(rdr, None)
				if terms == None:
					break
<<<<<<< HEAD
		return self


=======

		return self
>>>>>>> master
class mtmplt(object):
	'''Load object that can retrieve mtmplt from default tmplt store'''
	def __init__(self):
		self.mtmplts = fonql.doc(path).read()
<<<<<<< HEAD

=======
>>>>>>> master
	def search(self):
		''' '''


<<<<<<< HEAD
#==============================Source Materials=================================||
'''
=======

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
>>>>>>> master
''' #																			||
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
