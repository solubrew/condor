#@@@@@@@@@@@@@@@@@@@Config.Config@@@@@@@@@@@@@@@@@@@@@@||
'''
---
<(META)>:
	docid: 'aff91b21-e389-4114-b3ba-bf7f65e98002'
	name: Test Condor Module Python Document
	description: >
	expirary: <[expiration]>
	version: <[version]>
	authority: document|this
	security: seclvl2
	<(wt)>: -32
'''
# -*- coding: utf-8 -*-
#===============================================================================||
from os.path import abspath, dirname, isdir, isfile, join
import pprint
#===============================================================================||
import crow
#===============================================================================||
from condor import condor#									||
from excalc import tree as calctr
#========================Common Globals=========================================||
here = join(dirname(__file__),'')#												||
there = abspath(join('../../..'))#												||set path at pheonix level
version = '0.0.0.0.0.0'#														||
log = True
pp = pprint.PrettyPrinter(indent=4)
#===============================================================================||

def run():
	''' '''
	test_0002()

def test_0001():
	f0 = f'{here}_data_/test_0002_0.yaml'
	cfg = condor.instruct(f0)
	f1 = f'{here}_data_/test_0002_1.yaml'
	cfg.override(f1)
	if log: print('CFG', cfg.dikt)

def test_0002():
	''' '''
	f0 = join(abspath(here), '_data_/session.yaml')
	cfg = condor.instruct(f0).load().dikt
	if log: print('CFG', cfg)

if __name__ == '__main__':
	run()


#==============================Source Materials=================================||
'''

'''
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@||
