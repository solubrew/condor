# @@@@@@@@@@@@@@@@@@@Config.Config@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid: 1b83f5b6-3b4a-437d-a8f1-372d2220125e
	name: Elements Level Config Module Python Document
	description: >
		Load configuration files and parse using a given
		template
	expirary: <[expiration]>
	version: '0.0.0.0.0.0'
	authority: document|this
	security: seclvl2
	<(WT)>: -32
"""
import json
from importlib import import_module  # ||
from os import listdir
# -*- coding: utf-8 -*-
# ===============================================================================||
from os.path import abspath, dirname, expanduser, isfile, join

from ogma.logma import Logma
from subtrix import subtrix, thing

# ===============================================================================||
from condor import session

# ========================Common Globals=========================================||
here = join(dirname(__file__), '')  # ||
home = expanduser('~')
log = False
logma = Logma(__name__)
# ===============================================================================||
pxcfg = join(abspath(here), '_data_', 'condor.yaml')  # ||use default configuration


class Instruct(object):  # ||
	"""Load Configuration Files with cascading override of templates"""  # ||

	def __init__(self, it=None, data={}, prime=None, cfg=None):
		self.config = self.load(pxcfg, 'thing')
		self.session = session.POV().sessions()
		self.prime = self.session.prime
		self.ppov = self.session.ppov
		self.data = data
		self.thing = it
		self.dikt = {}

	def addArgs(self, args):
		""" """
		self.dikt['args'] = args
		return self

	def commit(self, writer_object=None):
		"""
		Store config data permanately using the provided or default writer object
		"""

	def clearMeta(self):
		"""
		remove meta keys from condor config files
		"""
		[self.dikt.pop(i) for i in ['<(META)>', '<(meta)>', '<(DNA)>', '<(dna)>'] if i in self.dikt.keys()]
		return self  # ||

	def load(self, this=None, how=None):  # ||
		"""Load File or Directory"""  # ||
		if this is None:
			this = self.thing
		self.dikt, self.text = load(this, how)
		self.clearMeta()
		return self

	def modulize(self, extobjs=[]):
		"""Import dotted path text and return the attribute/class"""
		module_path = None
		self.obj = None
		if '.' in self.thing:
			try:
				module_path, class_name = self.thing.rsplit('.', 1)
			except Exception as e:
				logma.warning(f'{e} Config.Modulize {self.thing}')
		if module_path is not None:
			module = import_module(module_path)
			try:  # ||
				self.obj = getattr(module, class_name)
			except AttributeError as e:  # ||
				logma.warning('config modulize {e}')
		return self  # ||

	def override(self, updates, loadType=None):  # ||
		"""override configuration with branch grafts"""  # ||
		if log: logma.info(f'Override Updates {updates}')
		if self.dikt == {} or self.dikt == None:
			self.load()  # ||
		if isinstance(updates, instruct):
			updates = updates.dikt
		if isinstance(updates, str):
			updates, text = load(updates, loadType)  # ||
		if updates != None:  # ||
			if log: logma.info(f'Override Updates {type(updates)}')
			if log: logma.info(f"{self.dikt} {updates}")
			self.dikt = merge_data(self.dikt, updates, 'override')
			if log: logma.info(f'Overriden {self.dikt}')
		return self  # need to fix this to make configuration files additive

	def select(self, what, frum=None):  # ||
		"""Select subtree of YAML document from top level branches"""  # ||
		if self.dikt == {}:
			self.load(frum)  # ||
		if not isinstance(what, list):
			what = [what, ]
		for wha in what:
			if wha in self.dikt.keys():  # ||
				self.dikt = self.dikt[wha]  # ||
		return self  # ||

	def sessionize(self, it):  # ||
		"""Apply session information to the given"""  # ||
		return subtrix.Mechanism(it, self.pov).run().it  # ||

	def selfFill(self):
		""" """
		self.load()
		self.text = subtrix.Mechanism(self.text, self.dikt).run().it
		if log: logma.info(f'TEXT {self.text}')
		self.dikt, self.text = load(self.text)
		return self

	def _seshSub(self):
		""" """
		inputs = self.session.ppov
		self.text = subtrix.Mechanism(self.text, inputs).run().it[0]
		self.dikt, self.text = load(self.text)
		return self


class instruct(Instruct):
	"""2024-01-24 backwards compatability"""

	def __init__(self, it=None, data={}, prime=None, cfg=None):  # ||
		Instruct.__init__(self, it, data, prime, cfg)

def load(this, how=None):
	"""Load configuration"""
	if log: logma.info(f'This {this}')
	if this == None:
		return {}, ''
	if isinstance(this, dict):
		text = json.dumps(this)
	elif isfile(this):  # ||
		if log: logma.info(f'This is a file {this}')
		if how == 'thing':
			dikt = thing.What(this).load().dikt  # ||
		else:
			dikt = thing.What(this).load().dikt
		if log: logma.info(f'Load Dikt {dikt}')
		text = json.dumps(dikt)
	# elif isdir(this):  #Not sure this is useful
	# 	dikt = fonql.doc(this).read()
	# 	text = calctr.stuff(dikt).dict2str().it
	elif isinstance(this, instruct):
		dikt, text = this.dikt, this.text
	elif isinstance(this, str):
		try:
			dikt = json.loads(this)
		except:
			dikt = {}
		text = this
	else:  # ||
		if log: logma.info(f'Config Loader not able to handle {this}')
		dikt, text = {}, ''  # ||
	if dikt == None:
		dikt, text = {}, ''
	return dikt, text


def loaddir(path: str, how=None):
	"""Load a directory full of yaml files into config overriding in
		alphabetical order

		implement other sorting possiblities and mappings

		"""
	cnt = 0  # ||
	for f in listdir(path):
		if cnt == 0:  # ||
			cfg = instruct(f'{path}/{f}').load()  # ||
			cnt = 1  # ||
		else:  # ||
			cfg.override(f'{path}/{f}')  # ||
	return cfg


def merge_data(dikt, merge_dikt=None, how='keep'):  # ||
	"""Recursively merge dicts nested to an arbitrary depth
		keep:=> controls wether to combine in an additive way to override old data
		maximize:=> tells the function wether to allow None replacements of
					current data...not currently implemented
	"""  # ||
	if isinstance(merge_dikt, dict):  # ||
		for k, v in merge_dikt.items():  # ||
			if v == 'null':
				v = None
			if isinstance(dikt, dict):
				if k in dikt.keys() and isinstance(dikt[k], dict):  # ||
					merge = merge_data(dikt[k], merge_dikt[k], how)  # ||
					if merge == 'null':
						merge = None
					if not isinstance(merge, (dict, list)):  # ||
						if merge == None or how == 'override':  # ||
							if log: logma.info(f'Merge {merge}')
							dikt[k] = merge  # ||
						else:  # ||
							if log: logma.info(f'Make list Merge {merge}')
							dikt[k] = [merge]  # ||
					else:  # ||
						dikt[k] = merge  # ||
				else:  # ||
					if k in dikt.keys():  #
						if log: logma.info(f'Dikt Keys {k}')
						v = dikt[k]  #
						if v == 'null':
							v = None
						if merge_dikt[k] == 'null':
							merge_dikt[k] = None
						if v == None or how == 'override':
							if log: logma.info('Override', merge_dikt[k], v)
							dikt[k] = merge_dikt[k]  # ||changed this line for the below 20200928
						else:
							if not isinstance(v, list) and merge_dikt[k]:
								logma.info(f'Make list {v} {merge_dikt[k]} How {how}')
								dikt[k] = [v]
								if isinstance(merge_dikt[k], list):
									dikt[k] += merge_dikt[k]
								else:
									if merge_dikt[k] not in dikt[k]:
										dikt[k].append(merge_dikt[k])
							else:
								dikt[k] = v
					else:
						if log: logma.info(f'Merge_Dikt {merge_dikt[k]}')
						dikt[k] = merge_dikt[k]
	elif isinstance(merge_dikt, str):
		return merge_dikt
	return dikt  # ||


# ==============================Source Materials=================================||
"""
"""
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
