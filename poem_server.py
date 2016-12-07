#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim: set bg=dark noet sw=4 ts=4 fdm=indent : 

"""Poem Server """
__author__='chutong'

import os
import sys
import logging
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

	basepath = os.path.abspath(os.getcwd())
	confpath = os.path.join(basepath, 'conf/poem.conf')
	conf = ConfigParser.RawConfigParser()
	conf.read(confpath)
	logging.basicConfig(filename=os.path.join(basepath, 'logs/poem_service.log'), level=logging.DEBUG,
		format = '[%(filename)s:%(lineno)s - %(funcName)s %(asctime)s;%(levelname)s] %(message)s',
		datefmt = '%Y-%m-%d %H:%M:%S')

	logger = logging.getLogger("PoemServer")
	try:
		host = conf.get('db', 'host')
		port = conf.get('db', 'port')

		omg_server = OmgServer(conf)
		processor = OmgService.Processor(omg_server)
		transport = TSocket.TServerSocket(host, port)
		tfactory = TTransport.TFramedTransportFactory()
		pfactory = TBinaryProtocol.TBinaryProtocolFactory()
		server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory, daemon=True)

		logger.info('poem service start')
		server.serve()
	except Exception as e:
		logger.exception(e)
