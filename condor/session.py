# @@@@@@@@@@@@@@@@@@Condor.Session@@@@@@@@@@@@@@@@@@@@@@||
""" #																			||
--- #																			||
<(META)>: #																		||
	DOCid: 133f1925-a7f4-4b52-9f29-97b62a825961 #								||
	name: > #																	||
		&ELCMSEPD  Module Session Extension Python Document #										||
	description: > #															||
		Create, Maintain, and Archive sessions. A session control #				||
		entry into the LEXI system from each Actor for managing #				||
		all POVs #																||
	expirary: <[expiration]> #													||
	outline: <[outline]> #														||
	authority: document|this #													||
	security: sec|lvl2 #														||
	<(WT)>: -32 #																||
"""  # ||
# -*- coding: utf-8 -*-#														||
# ==================================Core Modules=================================||
from os.path import abspath, dirname, join, exists  # ||

from ogma.logma import Logma
from roads.condor import getLEXIconfig
# ===============================================================================||
from subtrix import thing

# ================Common Globals=================================================||
here = join(dirname(__file__), '')  # ||
log = False
logma = Logma(__name__)

# ===============================================================================||
pxcfg = join(abspath(here), '_data_', 'session.yaml')  # ||use default configuration


class POV(object):  # ||
	'Load the Point-Of-View Initiating the Instance'  # ||

	def __init__(self):  # ||
		self.config = thing.What().get(pxcfg)  # ||
		self.session = {}  # ||
		lexi = thing.What().uuid().ruuid  # ||
		self.lexiv = self.config.dikt['LEXIvrs']  # TODO: needs redesigned
		self.where = thing.Where()  # ||
		self.who = thing.Who()  # ||
		self.homev = self.where.device().home  # ||
		self.bearv = f'{self.lexiv}/bear/'  # ||
		self.actors, self.concerns = {}, {}  # ||
		self.prime()  # ||

	def prime(self):  # ||
		'Load Prime Point of View'  # ||
		prime = {}
		cfg_type = ''
		primefile = getLEXIconfig('desktop')
		if log: logma.info(primefile)
		if exists(primefile):
			prime = thing.What().get(primefile).dikt
		else:
			prime = thing.What().get(getLEXIconfig('docker')).dikt
		if log: logma.info(f'Prime {prime}')
		self.prime = prime['prime']
		self.concern = prime['concern']
		ppovfile = f'{self.bearv}{self.concern}/{self.prime}.yaml'  # ||
		if log: logma.info(f'Load PPOV File {ppovfile}')
		self.ppov = thing.What().get(ppovfile).dikt  # ||load prime pov file
		if log: logma.info(f'PPOV {self.ppov}')
		return self  # ||

	def loadActors(self):
		""" """
		for actor in self.ppov['povs']['actors']:
			self.actors[actor] = actor(actor)
		return self

	def loadConcerns(self):
		""" """
		for concern in self.ppov['povs']['concerns']:
			self.concerns[concern] = concern(concern)
		return self

	def loadTmplts(self):  # ||
		""" """
		self.tmplts = tmplts(f'{self.bearv}LEXI/TMPLTs/')  # ||
		self.mtmplts = mtmplts(f'{self.bearv}LEXI/MTMPLTs/')  # ||
		return self  # ||

	def sessions(self, lvl='active'):  # ||
		"""
		create simple session
		"""
		if log: logma.info(f"PPOV {self.ppov}")
		povs = self.ppov['povs']  # ||
		actors = povs['actors']  # ||
		self.seshs = []  # ||
		self.combine()  # ||
		self.data = {'POV': povs, 'LEXIvrs': self.lexiv, 'DATAvrs': '', 'VEINvrs': '', 'bearvrs': self.bearv}
		return self  # ||

	def create(self, expiration=None):  # ||
		'Create a new session for the actor'  # ||
		if expiration == None:  # ||
			expiration = '5D'  # ||
		tnow = thing.when()  # ||
		dates = tmap.build(tnow.now, None, expiration)  # ||
		newseshid = tnow.dtid  # ||generate new sessionid
		tpath = self.bear + 'template'  # ||
		tmplt = thing.what().get(tpath)  # ||
		if log: print(newseshid)  # ||
		self.expiration = tmap.thing().window()  # ||
		return self  # ||

	def combine(self):  # ||
		'Load Active Sessions'  # ||
		for sesh in self.seshs:  # ||
			pass  # ||
		return self  # ||

	def action(self):  # ||
		''  # ||
		return self  # ||

	def retire(self):  # ||
		"""Move session from active to sleep for transitioning of data"""  # ||
		sseshs = os.listdir(f'{spath}1_sleep')  # ||
		tpath = f'{lexiv}bear/'  # ||
		tmpltSession = lexiv  # ||
		session = thing.what().get(this).dikt  # ||
		return self  # ||

	def terminate(self):  # ||
		"""Move session from sleep to kill for finalization of data history"""  # ||
		kseshs = os.listdir(f'{spath}2_kill')  # ||
		return self  # ||


class Session:
	def __init__(self):
		self.life = 1

	def role(self):  # must be passed a defined actor data chunk
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

# ==============================Source Materials=================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
