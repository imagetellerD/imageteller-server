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
from omg_poem import OmgPoemGenerator

class OmgServer(object):
	""" Omg Server"""
	def __init__(self, conf):
		self.logger = logging.getLogger("omg.server")
		self.helper = OmgHelper(conf)
		self.poem_generator = OmgPoemGenerator(conf)

	def test(self, id):
		t = Test()
		t.id = id
		t.name = "test"
		self.logger.info('server serve %d %s ', t.id, t.name)
		return t

	def generatePoem(self, title, tags, description):
		self.logger.info('generatePoem works')
		try:
			return self.poem_generator.generatePoem(title, tags, description)
		except Exception, e:
			raise OmgException(code=OmgServiceCode.ERROR_SYSTEM_ERROR, message="%s"%e)

	def searchCreativeTexts(self, tags, description):
		try:
			return self.helper.searchCreativeTexts(tags, description)
		except Exception, e:
			self.logger.error(e)
			raise OmgException(code=OmgServiceCode.ERROR_SYSTEM_ERROR, message="%s"%e)
	
	def analyzeImage(self, data_type, image_data, language):
		try:
			return self.helper.analyzeImage(data_type, image_data, language)
		except Exception, e:
			raise OmgException(code=OmgServiceCode.ERROR_SYSTEM_ERROR, message="%s"%e)

