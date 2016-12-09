#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim: set bg=dark noet sw=4 ts=4 fdm=indent : 

"""Poem Mock Client"""
__author__='chutong'

import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")
basepath = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/../')
sys.path.append(basepath + '/lib')
sys.path.append(basepath + '/lib/gen-py')

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


if  __name__ == '__main__':

	filedir = os.path.dirname(__file__)
	if filedir == '':
		filedir = '.'
	basepath = filedir+'/../'
	confpath = os.path.join(basepath, 'conf/imageteller.conf')
	conf = ConfigParser.RawConfigParser()
	conf.read(confpath)
	logging.basicConfig(filename=os.path.join(basepath, 'logs/poem_client.log'), level=logging.DEBUG,
		format = '[%(filename)s:%(lineno)s - %(funcName)s %(asctime)s;%(levelname)s] %(message)s',
		datefmt = '%Y-%m-%d %H:%M:%S')

	logger = logging.getLogger("PoemClient")
	try:
		host = conf.get('db', 'host')
		port = conf.get('db', 'port')

		transport = TSocket.TSocket(host, port)
		transport = TTransport.TFramedTransport(transport)
		protocol = TBinaryProtocol.TBinaryProtocol(transport)
		client = OmgService.Client(protocol) 
		transport.open()
		try:
			print 'client call'
			result = client.test(123)
			print 'test result ', result

			tags = []
			for i in range(2):
				tag = ImageTag()
				tag.tag = "菊花"
				tag.confidence = 0.9
				tags.append(tag)
			
			result = client.generatePoem("浣溪沙", tags, ['description', 'description'])
			print 'generatePoem result ', result
			
			result = client.searchCreativeTexts(['fight', 'message'], ['game fantastic', 'just fun'])
	#		result = client.searchCreativeTexts(['tag1', 'tag2'], ['no description', 'description is'])
			print 'searchCreativeTexts result ', result
		except Exception as e:
			logger.exception(e)
		finally:
			transport.close()

	except Exception as e:
		logger.exception(e)
