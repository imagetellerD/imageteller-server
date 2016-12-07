#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim: set bg=dark noet sw=4 ts=4 fdm=indent : 

"""Omg helper """
__author__='lizhengxu'

import logging
from domob_thrift.omg_types.ttypes import *
from domob_thrift.omg_types.constants import *
from domob_thrift.omg.ttypes import *
from domob_thrift.omg.constants import *
from domob_thrift.omg_common.ttypes import *


class OmgHelper(object):
	""" Omg Server"""
	def __init__(self):
		self.logger = logging.getLogger("omg.helper")

	def searchCreativeTexts(self, tags, descriptions):
		self.logger.info('searchCreativeTexts works')
		return ['OK', 'OK']
