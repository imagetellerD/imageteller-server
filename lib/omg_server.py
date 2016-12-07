#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim: set bg=dark noet sw=4 ts=4 fdm=indent : 

"""Omg Server """
__author__='chutong'

import logging
from domob_thrift.omg_types.ttypes import *
from domob_thrift.omg_types.constants import *
from domob_thrift.omg.ttypes import *
from domob_thrift.omg.constants import *
from domob_thrift.omg_common.ttypes import *

from omg_helper import OmgHelper

class OmgServer(object):
	""" Omg Server"""
	def __init__(self, conf):
		self.logger = logging.getLogger("omg.server")
		self.helper = OmgHelper()

	def test(self, id):
		t = Test()
		t.id = id
		t.name = "test"
		self.logger.info('server serve %d %s ', t.id, t.name)
		return t

	def generatePoem(self, title, tags, description):
		try:
			self.logger.info('generatePoem works')
			return "OK"
		except Exception, e:
			raise OmgException(code=OmgServiceCode.ERROR_SYSTEM_ERROR, message="%s"%e)

	def searchCreativeTexts(self, tags, description):
		try:
			return self.helper.searchCreativeTexts(tags, description)
		except Exception, e:
			raise OmgException(code=OmgServiceCode.ERROR_SYSTEM_ERROR, message="%s"%e)
			
