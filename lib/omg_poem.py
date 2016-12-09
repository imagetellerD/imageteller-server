#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim: set bg=dark noet sw=4 ts=4 fdm=indent : 

"""Omg poem generator """
__author__='chutong'

import os
import sys
reload(sys)
sys.setdefaultencoding("utf8")
sys.path.append("/home/chutong/.local/lib/python2.7/site-packages")

import logging
from domob_thrift.omg_types.ttypes import *
from domob_thrift.omg_types.constants import *
from domob_thrift.omg.ttypes import *
from domob_thrift.omg.constants import *
from domob_thrift.omg_common.ttypes import *

from poem_generator.generator import Generator 

basepath = os.path.abspath(os.path.dirname(__file__))


class OmgPoemGenerator(object):
	def __init__(self, conf):
		self.conf = conf

	def generatePoem(self, title, tags, descriptions):
		logger = logging.getLogger('omg.poem')
		logger.info("generate poem begins")

		generator = Generator(basepath, self.conf)
		try:
			# As user input, for theme of poem, and title
			#user_input_dict = dict(title=u"浣溪沙", important_words=[u"菊花", u"院子"], force_data_build=False)

			# str to unicode
			title = title.decode()
			important_words = []
			for tag in tags:
				important_words.append(tag.tag.decode())

			logger.info("user input title %s, important_words %s, descriptions %s" % (title, str(important_words), str(descriptions)))
			user_input_dict = dict(title=title, important_words=important_words, descriptions=descriptions, force_data_build=False)

			# Init
			generator.force_data_build = user_input_dict["force_data_build"]
			generator.init(logger)

			# Generate poem
			error_info = generator.check(user_input_dict, logger)
			if not error_info:
				generator.title = user_input_dict["title"]
				generator.important_words = user_input_dict["important_words"]
			
				logger.info("generate poem for title %s, with important words %s" % (generator.title, str(generator.important_words)))
				result = generator.generate(logger)
			else:
				result = error_info
			logger.info("final generate poem %s" % result)
			   
		except ValueError as e:
			logger.exception(e)
		except Exception as e:
			logger.exception(e)
		finally:
			return result.encode()
