#@@@@@@@@@@@@@@@@@@@Config.Config@@@@@@@@@@@@@@@@@@@@@@||
'''
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
'''
# -*- coding: utf-8 -*-
#===============================================================================||
from os.path import abspath, dirname, expanduser, isdir, isfile, join
import datetime as dt, copy#													||
from importlib import import_module#											||
#===============================================================================||
from condor import session, thing#												||
from excalc import tree as calctr#								||
from squirl.orgnql import fonql, yonql
from subtrix import subtrix#													||
#========================Instance Globals=======================================||
'Generate an Instance uuid for the initiation point in a session'#				||
if 'povsesh' not in globals():#													||
	global povsesh#																||
	povsesh = session.pov().sessions()#											||
#========================Common Globals=========================================||
here = join(dirname(__file__),'')#												||
home = expanduser('~')
log = False
#===============================================================================||
pxcfg = join(abspath(here), '_data_/config.yaml')#								||use default configuration
class instruct:#																||
	'Load Configuration Files with cascading override of templates'#			||
	def __init__(self, it=None, data={}, prime=None, cfg=None):#				||
		self.config = self.load(pxcfg, 'thing', None).dikt#						||
		self.session = povsesh#													||
		self.prime = povsesh.prime#												||
		self.ppov = povsesh.ppov#												||
		self.data = data#														||
		self.thing = it
		self.dikt = {}

	def addArgs(self, args):
		''' '''
		self.dikt['args'] = args
		return self

	def branchByIDSearch(self, term):#									||
		'find the term in list of ids and then return parent tree'
		branches = calctr.stuff(self.dikt).search('IDs')
		for branch in branches:
			if term in branch.values():
				self.parameter = branch['parent']
		return self

	def expand(self, base=None):#										||
		''#																||
		if base == None:#												||
			base = self.dikt#											||
		base, lock = calctr.stuff(base), 1#								||
		while lock == 1:#												||
			path = base.search('paths')#								||
			if path == None:#											||
				lock = 0#												||
			else:#														||
				update = self.load(path).dikt#							||
				base.graft(update)#										||
		return self#													||

	def getEntries(self, limit=None):
		if self.dikt != None:#											||
			self.entries = self.dikt.keys()#							||
		else:#															||
			self.entries = None#										||
		if limit == None:
			iis = ['<(META)>', '<(meta)>', '<(DNA)>', '<(dna)>']
			for i in iis:
				try:
					self.dikt.pop(i)
				except:
					pass
		return self#													||

	def known(self, what=None):#										||
		''#
		paths = []#														||
		if what == None:#												||
			what = self.thing#											||
		if what == 'syntax':
			p = self.config['syntaxtypes']
		elif what == 'files':
			p = self.config['filetypes']
		self.dikt = self.load(p).dikt
		return self#													||

	def load(self, this=None, how=None, limit=None):#							||
		'''Load File or Directory'''#											||
		if this == None:
			this = self.thing
		self.dikt, self.text = load(this, how)
		self.getEntries(limit)
		return self

	def modulize(self, extobjs=[]):#											||
		'''Import dotted path text and return the attribute/class'''#				||
		if '.' in self.thing:#													||
			try:#																||
				module_path, class_name = self.thing.rsplit('.', 1)#			||
			except Exception as e:#												||
				print(e,'Config.Modulize', self.thing)
		module = import_module(module_path)#									||
		try:#																	||
			self.obj = getattr(module, class_name)#								||
		except AttributeError as e:#											||
			print('config modulize',e)
		return self#															||

	def override(self, updates, loadType=None):#							||
		'''override configuration with branch grafts'''#						||
		if log: print('Override Updates', updates)
		if self.dikt == {} or self.dikt == None:
			self.load()#														||
		if isinstance(updates, instruct):
			updates = updates.dikt
		if isinstance(updates, str):
			updates, text = load(updates, loadType)#									||
		if updates != None:#													||
			if log: print('Override Updates', type(updates))
			if log: print(self.dikt, updates)
			self.dikt = calctr.merger(self.dikt, updates, 'override')
			if log: print('Overriden', self.dikt)
		return self#		need to fix this to make configuration files additive

	def select(self, what, frum=None):#											||
		'''Select subtree of YAML document from top level branches'''#				||
		if self.dikt == {}:
			self.load(frum)#													||
		if not isinstance(what, list):
			what = [what,]
		for wha in what:
			if wha in self.dikt.keys():#								||
				self.dikt = self.dikt[wha]#										||
		return self#															||

	def sessionize(self, it):#													||
		'''Apply session information to the given'''#								||
		return subtrix.mechanism(it, self.pov).run().it#							||

	def selfFill(self):
		''' '''
		self.load()
		self.text = subtrix.mechanism(self.text, self.dikt).run().it
		if log: print('TEXT', self.text)
		self.dikt, self.text = load(self.text)
		return self

	def _seshSub(self):
		''' '''
		inputs = self.session.ppov
		self.text = subtrix.mechanism(self.text, inputs).run().it[0]
		self.dikt, self.text = load(self.text)
		return self


def load(this, how=None):
	'''Load configuration'''
	if log: print(f'This {this}')
	if this == None:
		return {}, ''
	if isinstance(this, dict):
		dikt = this
		text = calctr.stuff(dikt).dict2str().it
	elif isfile(this):#											||
		if log: print('This is a file', this)
		if how == 'thing':
			dikt = thing.what(this).get().dikt#								||
		else:
			dikt = next(yonql.doc(this).read()).dikt
		text = calctr.stuff(dikt).dict_2_str().it
	elif isdir(this):#											||
		dikt = fonql.doc(this).read()#								||
		text = calctr.stuff(dikt).dict2str().it
	elif isinstance(this, instruct):
		dikt, text = this.dikt, this.text
	elif isinstance(this, str):
		try:
			dikt = json.loads(this)
		except:
			dikt = {}
		text = this
	else:#																||
		if log: print('Config Loader not able to handle {this}')
		dikt, text = {}, ''#													||
	if dikt == None:
		dikt, text = {}, ''
	return dikt, text

def loaddir(path: str, how=None):
	'''Load a directory full of yaml files into config overriding in
		alphabetical order

		implement other sorting possiblities and mappings

		'''
	cnt = 0#																	||
	for f in listdir(path):
		if cnt == 0:#															||
			cfg = instruct(f'{path}/{f}').load()#				||
			cnt = 1#															||
		else:#																	||
			cfg.override(f'{path}/{f}')#								||
	return cfg


#==============================Source Materials=================================||
'''

'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
