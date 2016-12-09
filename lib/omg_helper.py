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
from microsoft_api import MicrosoftApi

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

	def analyzeImage(self, data_type, image_data, language):
		self.logger.info('begin to analyze image...');
		analystResult = ImageAnalyzeResult()
		analystResult.tags = []
		analystResult.descriptions = []
		microsoftApi = MicrosoftApi(self.cfg)
		if language == ImageAnalyzeLanguage.IAL_CN:
			language = 'zh'
		else:
			language = 'en'

		if data_type == ImageDataType.IDT_URL:
			data = microsoftApi.analyzeImageThroughUrl(image_data.image_url, language)
			#print data
			if data and (data.has_key('tags') or data.has_key('description')):
				self.logger.info('get analyze image data success');
				for tag in data['tags']:
					_tag = ImageTag()
					_tag.tag = tag['name'].encode('utf-8')
					_tag.confidence = int(tag['confidence'] * 100)
					analystResult.tags.append(_tag)
				for desc in data['description']:
					analystResult.descriptions.append(desc.encode('utf-8'))
			else:
				self.logger.info('get analyze image data failed');
			#cloudsight todo
		#else :
			#pass
		self.logger.info('analyze image over...');
		return analystResult
		

	def searchCreativeTexts(self, tags, descriptions):
		self.logger.info('searchCreativeTexts works')

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
