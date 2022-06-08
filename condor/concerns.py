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

#===============================================================================||
from condor import condor
#===============================================================================||
here = join(dirname(__file__),'')#						||
there = abspath(join('../../..'))#												||set path at pheonix level
version = '0.0.0.0.0.0'#												||
wolfpack = '{0}wolf/pack/bash'.format(there)
#===============================================================================||
class actor(object):
	def __init__(self, actor, cfg={}):
		'''Actor object implements permissions and roles for access to work and
		assests where the actor is an independant action taker mostly human
		operators but the possibility of a nearly automous bot as well'''
		path = '<(BEARvrs)>{0}/{0}.yaml'.format(actor)
		pxcfg = subtrix.mechanism(path).run()[0]
		self.config = config.insturct(pxcfg).override(cfg)
		self.pov = self.config.dikt['ppov']
		self.actor = actor

	def loadCFGs(self):
		''' '''
	def loadOP(self):
		''' '''
	def loadDATA(self):
		''' '''
	def searchOPs(self):
		''' '''
	def searchDATA(self):
		''' '''



class concern(object):
	def __init__(self, concern, cfg=None):
		'''Concern object implements permissions and roles for access to work
			and assets where an actor has entanglements with that concern'''
		self.path = '<(BEARvrs)>{0}/'.format(concern)
		path = '{0}{1}.yaml'.format(self.path, concern)
		pxcfg = subtrix.mechanism(path).run()[0]
		self.config = config.insturct(pxcfg).override(cfg)
		self.pov = self.config.dikt['ppov']
		self.concern = concern
	def loadCFGs(self):
		''' '''
	def loadOP(self, op):
		''' '''
		if isinstance(op, str):
			fnd, op = self.searchOPs(op)
			if fnd == False:
				return False, None

	def loadDATA(self, data):
		'''Load data from known location if given data is a dict however if it
			is a string then search known data for given data term'''
		if isinstance(op, str):
			fnd, op = self.searchOPs(op)
			if fnd == False:
				return False, None
	def searchOPs(self):
		'''Search for Operations connected to concern '''
		path = '{0}OPs'.format(self.path)
		self.opfiles = fonql.doc(path).filtr('.yaml').read()
		while True:
			opfiles = next(self.opfiles, None)
			if opfiles == None:
				break
			for opfile in self.opfiles:
				ops = yonql.doc(opfile).read().dikt
				for op in ops:
					if term == op:
						return True, op
		return False, None
	def searchDATA(self):
		'''Search for data connected to concern '''



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
