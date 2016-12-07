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

import sys
sys.path.append("/home/zeus/lizhengxu/hack/python-lib/lib/python2.7/site-packages")

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError
from elasticsearch.client import IndicesClient
import string

class OmgHelper(object):
	""" Omg Helper"""
	def __init__(self, conf):
		self.cfg = conf

		self.logger = logging.getLogger("omg.helper")

		self.es_hosts = self.cfg.get('elasticsearch', 'hosts')
		self.es_index = self.cfg.get('elasticsearch', 'index')
		self.es_type = self.cfg.get('elasticsearch', 'type')
		self.es_analyzer = self.cfg.get('elasticsearch', 'analyzer')
		self.es_timeout = self.cfg.getint('elasticsearch', 'timeout')
		self.es_size = self.cfg.getint('elasticsearch', 'size')
		self.es_tag_weight = self.cfg.getint('elasticsearch', 'tag.weight')
		self.es_minimum_should_match = self.cfg.getint('elasticsearch', 'minimum.should.match')

	def searchCreativeTexts(self, tags, descriptions):
		self.logger.info('searchCreativeTexts works')

		# TODO 连接池
		esClient = Elasticsearch(hosts=self.es_hosts.strip().split(","))

		descriptionstr = str()
		for tag in tags:
			descriptionstr += tag + ' '

		for desccription in descriptions:
			descriptionstr += desccription + '. '

		self.logger.debug("desciption:[%s]", descriptionstr)

		# 通过es的分词功能处理 descriptionstr
		analyzeRes = esClient.indices.analyze(
			index=self.es_index, analyzer=self.es_analyzer,
			text=descriptionstr
			)

		querys = set()
		for token in analyzeRes['tokens']:
			querys.add(token['token'])

		querystr = string.join(querys)
		self.logger.debug("querys:[%s]", querystr)

		# 查询 es 获取结果
		response = esClient.search(
			index=self.es_index,
			body={
				"query": {
					"multi_match": {
						"query": querystr,
						"type": "best_fields",
						"fields": ["tags^%d"%self.es_tag_weight, "mesg"],
						"minimum_should_match": "%d"%self.es_minimum_should_match + "%"
					}
				}
			},
			analyzer=self.es_analyzer, size=self.es_size
			)

		creativeTexts = list()
		for i in range(response["hits"]["total"]):
			creativeTexts.append(response["hits"]["hits"][i]["_source"]["mesg"])

		return creativeTexts
