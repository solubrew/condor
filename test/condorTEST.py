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
from condor import condor
from ogma.logma import Logma

# ===============================================================================||
here = join(dirname(__file__), '')  # ||
log = True
logma = Logma(__name__)
# ===============================================================================||
pxcfg = join(abspath(here), '_data_', 'test_condor.yaml')  # ||use default configuration


class Test_Instruct(unittest.TestCase):
	""""""

	@classmethod
	def setup_class(cls):
		""" """
		cfg = {}
		cls.test_Instruct = condor.Instruct(cfg)
		return cls

	@classmethod
	def teardown_class(cls):
		""" """
		return

	def test_assert(self):
		""" """
		assert True

	def test_init(self):
		""""""
		logma.info('\n')
		logma.info(f"check self.config")
		assert isinstance(self.test_Instruct.config.dikt, dict)
		# check self.session
		logma.info(f"check Instruct.prime")
		assert isinstance(self.test_Instruct.prime, str)
		# check self.ppov
		assert isinstance(self.test_Instruct.ppov, dict)
		# check self.data
		# check self.thing
		logma.info(f"Check Insturct.dikt")
		assert self.test_Instruct.dikt == {}

	def test_init_docker(self):
		"""
		test for configuration from a docker container
		"""

	def test_addArgs(self):
		""""""

	def test_clearMeta(self):
		""""""
		self.test_Instruct.clearMeta()
		assert '<(META)>' not in self.test_Instruct.dikt.keys()
		assert '<(meta)>' not in self.test_Instruct.dikt.keys()
		assert '<(DNA)>' not in self.test_Instruct.dikt.keys()
		assert '<(dna)>' not in self.test_Instruct.dikt.keys()

	def test_load(self):
		""""""
		path = join(here, '_data_', 'test_condor.yaml')
		self.test_Instruct.load(path)
		assert isinstance(self.test_Instruct.dikt, dict)
		# TODO: add check for details
		assert isinstance(self.test_Instruct.text, str)

	# TODO: add check for items in text

	def test_modulize(self):
		""""""
		self.test_Instruct.modulize()
		assert self.test_Instruct.obj is not None

	def test_override(self):
		""""""
		path = join(here, '_data_', 'test_condor.yaml')
		self.test_Instruct.override(path)
		assert isinstance(self.test_Instruct.dikt, dict)
		# TODO check for info from test_condor that was overriden from the original
		config = 'need other instruct object here'
		self.test_Instruct.override(config)

	def test_select(self):
		""""""
		self.test_Instruct.select()

	def test_sessionize(self):
		""""""
		self.test_Instruct.sessionize()

	def selfFill(self):
		""""""
		self.test_Instruct.selfFill()


def test_load():
	""""""


def test_loaddir():
	""""""


if __name__ == '__main__':
	unittest.main()

# ==============================Source Materials=================================||

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
