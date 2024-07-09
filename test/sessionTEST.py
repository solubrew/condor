# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
"""
---
<(META)>:
	docid:
	name:
	description: >
	expirary: <[expiration]>
	version: <[Version]>
	authority: document|this
	security: sec|lvl2
	<(WT)>: -32
"""
import unittest
# -*- coding: utf-8 -*-
# =======================================================================||
from os.path import abspath, dirname, join

# ===============================================================================||
import crow

crow.crowLoad('Condor', 'ALPHA')

# ===============================================================================||
from condor import session
from ogma.logma import Logma

# ===============================================================================||
here = join(dirname(__file__), '')  # ||
log = True
logma = Logma(__name__)
# ===============================================================================||
pxcfg = join(abspath(here), '_data_', 'test_session.yaml')  # ||use default configuration


class Test_POV(unittest.TestCase):
	""""""

	@classmethod
	def setup_class(cls):
		""" """
		cfg = {}
		cls.test_POV = session.POV(cfg)

	@classmethod
	def teardown_class(cls):
		""" """

	def test_init(self):
		""""""
		if log: logma.info("\n")

	# self.config
	# self.session
	# self.lexiv
	# self.where
	# self.who
	# self.homev
	# self.bearv
	# self.actors
	# self.concerns
	# self.prime
	# self.concern
	# self.ppov

	def test_loadActors(self):
		""""""

	def test_loadConcerns(self):
		""""""

	def test_loadTmplts(self):
		""""""

	def test_sessions(self):
		""""""

	def test_create(self):
		""""""

	def test_combine(self):
		""""""

	def test_action(self):
		""""""

	def test_retire(self):
		""""""

	def test_terminate(self):
		""""""


class Test_Session(unittest.TestCase):
	""""""

	@classmethod
	def setup_class(cls):
		""" """
		cfg = {}
		cls.test_Session = session.Session()

	@classmethod
	def teardown_class(cls):
		""" """


if __name__ == '__main__':
	unittest.main()

# ==============================Source Materials=================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
