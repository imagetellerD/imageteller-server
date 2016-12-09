#!/usr/bin/env python
#-*- coding: utf-8 -*-
# vim: set bg=dark noet sw=4 ts=4 fdm=indent : 

"""Microsoft vison api """
__author__='zhouting'

import logging
import httplib
import urllib
import base64
import json

class MicrosoftApi(object):
	"""Microsoft vison api """
	def __init__(self, conf):
		self.cfg = conf
		
		self.logger = logging.getLogger("omg.microsoft_api")
		
		#self.api_domain = 'api.cognitive.azure.cn'
		#self.api_path = '/vision/v1.0/analyze'
		self.api_domain = self.cfg.get('image_analyze_api', 'microsoft_domain') 
		self.api_path = self.cfg.get('image_analyze_api', 'microsoft_api_path') 
		self.api_token = self.cfg.get('image_analyze_api', 'microsoft_api_key')	

	def request(self, header_content_type, body, language):
		headers = {
			'Content-Type': header_content_type,
			'Ocp-Apim-Subscription-Key': self.api_token,
		}
		params = urllib.urlencode({
			'visualFeatures': 'Categories,Tags' if language == 'zh' else 'Categories,Tags,Description',
			'details': 'Celebrities',
			'language': language,
		})
		data = None
		#self.logger.info("%s\n%s?%s" % (self.api_domain, self.api_path, params))
		try :
			conn = httplib.HTTPSConnection(self.api_domain)
			conn.request("POST", "%s?%s" % (self.api_path, params), body, headers)
			response = conn.getresponse()
			if response.status == 200:
				data = json.loads(response.read())
				descriptions = []
				if data.has_key('description') and data['description'].has_key('captions'):
					for desc in data['description']['captions']:
						if desc.has_key('text'):
							descriptions.append(desc['text'])
				data['description'] = descriptions
				#print data['description']
					
			else:
				#print response.read()
				self.logger.warning('call microsoft api failed, code: %s, response: %s' % (response.status, response.read()))
		except Exception, e:
			#print e
			self.logger.warning('call  microsoft api failed, exception: %s' % e)
		return data

	def analyzeImageThroughUrl(self, image_url, language):
		#data = self.request('application/json', json.dumps({'url':image_url}))
		if language == 'zh':
			language = 'zh'
		else:
			language = 'en'
		return self.request('application/json', json.dumps({'url':image_url}), language)

	def analyzeImageThroughFilename(self, image_url):
		return None
		
	
