#@@@@@@@@@@@@@@@@@@Condor.Session@@@@@@@@@@@@@@@@@@@@@@||
''' #																			||
--- #																			||
<(META)>: #																		||
	DOCid: 133f1925-a7f4-4b52-9f29-97b62a825961 #								||
	name: > #																	||
		&ELCMSEPD Elements Level Config Module #								||
		Session Extension Python Document #										||
	description: > #															||
		Create, Maintain, and Archive sessions. A session control #				||
		entry into the LEXI system from each Actor for managing #				||
		all POVs #																||
	expirary: <[expiration]> #													||
	version: <[version]> #														||
	path: <[LEXIvrs]>pheonix/elements/config/session.py #						||
	outline: <[outline]> #														||
	authority: document|this #													||
	security: sec|lvl2 #														||
	<(WT)>: -32 #																||
'''#																			||
# -*- coding: utf-8 -*-#														||
#==================================Core Modules=================================||
from os.path import abspath, dirname, join#										||
from os import listdir
import datetime as dt, copy#												||
from importlib import import_module#											||
#===============================================================================||
from condor.concerns import concern, actor#					||
from condor.tmplts import tmplt, mtmplt#						||
from condor import thing#										||
#================Common Globals=================================================||
here = join(dirname(__file__),'')#												||
there = abspath(join('../../..'))#												||set path at pheonix level
where = abspath(join(''))#														||set path at pheonix level
version = '0.0.0.0.0.0'#														||
log = False
#===============================================================================||
pxcfg = join(abspath(here), '_data_/config.yaml')#							||use default configuration
class pov:#																		||
	'Load the Point-Of-View Initiating the Instance'#							||
	def __init__(self):#														||
		self.config = thing.what().get(pxcfg).dikt#								||
		self.session = {}#														||
		lexi = thing.what().uuid().ruuid#										||
		self.lexiv = self.config['LEXIvrs']#									||
		self.where = thing.where()#												||
		self.who = thing.who()#													||
		self.homev = self.where.device().home#									||
		self.bearv = f'{self.lexiv}/bear/'#							||
		self.actors, self.concerns = {}, {}#									||
		self.prime()#															||
	def prime(self):#															||
		'Load Prime Point of View'#												||
		try:#																	||
			primefile = f'{self.homev}/.config/lexi/prime.yaml'#		||
			prime = thing.what().get(primefile).dikt#								||
		except Exception as e:#																||
			print('Failed to load Prime Config File', e)
			primefile = 'HVC/SETUP/prime.yaml'#									||
			prime = thing.what().get(primefile).dikt#								||
		self.prime = prime['prime']#											||
		self.concern = prime['concern']#										||
		ppovfile = f'{self.bearv}{self.concern}/{self.prime}.yaml'#		||
		if log: print('Load PPOV File', ppovfile)
		self.ppov = thing.what().get(ppovfile).dikt#							||load prime pov file
		return self#															||
	def loadActors(self):
		''' '''
		for actor in self.ppov['povs']['actors']:
			self.actors[actor] = actor(actor)
		return self
	def loadConcerns(self):
		''' '''
		for concern in self.ppov['povs']['concerns']:
			self.concerns[concern] = concern(concern)
		return self
	def loadTmplts(self):#														||
		''' '''
		self.tmplts = tmplts(f'{self.bearv}LEXI/TMPLTs/')#				||
		self.mtmplts = mtmplts(f'{self.bearv}LEXI/MTMPLTs/')#			||
		return self#															||
	def sessions(self, lvl='active'):#											||
		'create simple session'#												||
		povs = self.ppov['povs']#												||
		actors = povs['actors']#												||
		concerns = povs['concerns']#											||
		self.seshs = []#														||
		for actor in actors:#													||
			spath = f'{self.bearv}{actor}/SESHs/'#								||
#			if lvl == 'active':#												||
#				self.seshs.append(listdir(f'{spath}0_active'))#		||
#			elif lvl == 'sleep':#												||
#				self.seshs.append(listdir(f'{spath}1_sleep'))#		||
#			elif lvl == 'kill':#												||
#				self.seshs.append(listdir(f'{spath}2_kill'))#		||
#		self.lastsesh = sorted(self.seshs[len(self.seshs)-1])#					||
		self.combine()#															||
		self.data = {'POV': povs, 'LEXIvrs': self.lexiv, 'DATAvrs': '',
										'VEINvrs': '', 'bearvrs': self.bearv}
		return self#															||
	def create(self, expiration=None):#											||
		'Create a new session for the actor'#									||
		if expiration == None:#													||
			expiration = '5D'#											||
		tnow = thing.when()#											||
		dates = tmap.build(tnow.now, None, expiration)#					||
		newseshid = tnow.dtid#											||generate new sessionid
		tpath = self.bear+'template'#									||
		tmplt = thing.what().get(tpath)#								||
		if log: print(newseshid)#												||
		self.expiration = tmap.thing().window()#						||
		return self#													||
	def combine(self):#													||
		'Load Active Sessions'#											||
		for sesh in self.seshs:#										||
			pass#														||
		return self#													||
	def action(self):#													||
		''#																		||
		return self#															||
	def retire(self):#															||
		'''Move session from active to sleep for transitioning of data'''#		||
		sseshs = os.listdir(f'{spath}1_sleep')#						||
		tpath = f'{lexiv}bear/'#										||
		tmpltSession = lexiv#													||
		session = thing.what().get(this).dikt#									||
		return self#															||
	def terminate(self):#														||
		'''Move session from sleep to kill for finalization of data history'''#	||
		kseshs = os.listdir(f'{spath}2_kill')#							||
		return self#													||
# import os
# import socket
# import platform
# import psutil
# print(os.environ['HOME'])
# if socket.gethostname().find('.') >= 0:
# 	name = socket.gethostname()
# else:
# 	name = socket.gethostbyaddr(socket.gethostname())[0]
# print(name)
# print(socket.gethostname())
# print(socket.gethostbyaddr(socket.gethostname()))
# print(os.name)
# print(platform.machine())
# print(platform.linux_distribution())
# print(platform.release())
# for p in psutil.disk_usage('/'):
# 	print(p/1000000)
#

class session:
	def __init__(self):
		self.life = 1
	def role(self):#must be passed a defined actor data chunk
		self.actor = actor
		self.where = where.home()
	def valuestate(self):
		rsrc = resource.container()
	def update(self, aspect):
		if type(aspect) == 'goal':
			pass
	def expire(self):
		pass
	def extend(self):
		pass
	def identity(self):
		pass
	def name(self):
		self.first = first
		self.middle = middle
		self.last = last
	def user(self):
		self.username = genUser(self.first, self.last)
		self.password = genPass()
	def address(self):
		self.number = ''
		self.street = ''
		self.city = ''
		self.state = ''
		self.zipcode = ''
		self.zipext = ''
	def ssn(self):
		self.number = ''
	def parents(self):
		self.mom = getParents('mom')
		self.dad = getParents('dad')
#	def byUser(self):#													||
#		'Load Prime, POV, & Device'#									||
#		data = {'prime': self.prime}#									||
#		primecfg = tmplt.thing(self.config['user'], data).run().it#		||
#		ndikt = self.load(primecfg).dikt#								||
#		usercfg = primecfg['stor']['configs']+'/'#						||
#		usercfg += cfg['meta']['name']+'.yaml'#							||
#		udikt = config.instruct(usercfg).load(None, None).dikt#			||
#		self.where = where.home()#										||
#		self.who = who.whom()#											||
#		self.override(udikt)#											||
#		return self#													||
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
