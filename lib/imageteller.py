#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim: set bg=dark noet sw=4 ts=4 fdm=indent : 

"""Poem Server """
__author__='chutong'

import os
import sys
basepath = os.path.realpath(os.path.dirname(__file__)+'/../')
sys.path.append(basepath+'/lib')
sys.path.append(basepath+'/lib/gen-py')
import logging.config
import argparse
try:
	import ConfigParser
except ImportError:
	import configparser as ConfigParser
from domob_thrift.omg_types.ttypes import *
from domob_thrift.omg_types.constants import *
from domob_thrift.omg.ttypes import *
from domob_thrift.omg.constants import *
from domob_thrift.omg import OmgService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer



class OmgServer(object):
	""" Omg Server"""
	def __init__(self, conf):
		pass

	def test(self, id):
		t = Test()
		t.id = id
		t.name = "test"
		print 'server serve ', t.id, t.name
		return t


if  __name__ == '__main__':
	'''
	basepath = os.path.abspath(os.getcwd())
	confpath = os.path.join(basepath, 'conf/poem.conf')
	conf = ConfigParser.RawConfigParser()
	conf.read(confpath)
	logging.basicConfig(filename=os.path.join(basepath, 'logs/imageteller.log'), level=logging.DEBUG,
		format = '[%(filename)s:%(lineno)s - %(funcName)s %(asctime)s;%(levelname)s] %(message)s',
		datefmt = '%Y-%m-%d %H:%M:%S')

	'''
	ap = argparse.ArgumentParser(description = 'domob omg imageteller')
	ap.add_argument('-d', '--executeDir', type = str,
		help = 'execute directory',
		default = basepath)

	args = ap.parse_args()
	print 'run imageteller at %s' % args.executeDir

	os.chdir(args.executeDir)

	logConfFile = args.executeDir+'/conf/logging.conf'
	logging.config.fileConfig(logConfFile)

	cfgfile = args.executeDir + '/conf/imageteller.conf'
	cfg = ConfigParser.RawConfigParser()
	cfg.read(cfgfile)

	logger = logging.getLogger("omg.imageteller")
	try:
		port = cfg.get('db', 'port')

		omg_server = OmgServer(cfg)
		processor = OmgService.Processor(omg_server)
		transport = TSocket.TServerSocket(port=port)
		tfactory = TTransport.TFramedTransportFactory()
		pfactory = TBinaryProtocol.TBinaryProtocolFactory()
		server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory, daemon=True)

		logger.info('poem service start')
		server.serve()
	except Exception as e:
		logger.exception(e)
