import sys
import json
if sys.version < '3':
	from urllib2 import urlopen
	from urllib import quote as urlquote
else:
	from urllib.request import urlopen
	from urllib.parse import quote as urlquote

UD_DEFID_URL = 'http://api.urbandictionary.com/v0/define?defid='
UD_DEFINE_URL = 'http://api.urbandictionary.com/v0/define?term='
UD_RANDOM_URL = 'http://api.urbandictionary.com/v0/random'

class UrbanDef():
	def __init__(self, word, definition, example, upvotes, downvotes):
		self.word = word
		self.definition = definition
		self.example = example
		self.upvotes = upvotes
		self.downvotes = downvotes

	def __cmp__(self, other):
		if (self.upvotes - other.upvotes) != 0:
			return self.upvotes - other.upvotes
		else:
			return other.downvotes - self.downvotes

	def __str__(self):
		return '%s: %s... (%d, %d)' % (
				self.word,
				self.definition[:30],
				self.upvotes,
				self.downvotes
			)

def _getUrbanJSON(url):
	try:
		f = urlopen(url)
		data = json.loads(f.read().decode('utf-8'))
		return data
	except Exception as e:
		print e
	finally:
		try:
			f.close()
		except NameError:
			pass

def _parseUrbanJSON(json, checkResultType=True):
	result = []
	if json is None or any(e in json for e in ('error', 'errors')):
		raise Exception('ud api: user input error')
	if checkResultType and json['result_type'] == 'no_results':
		return result
	for definition in json['list']:
		d = UrbanDef(
				definition['word'], 
				definition['definition'],
				definition['example'],
				int(definition['thumbs_up']),
				int(definition['thumbs_down'])
			)
		result.append(d)
	return result

def define(term):
	json = _getUrbanJSON(UD_DEFINE_URL + urlquote(term))
	return _parseUrbanJSON(json)

def defineID(defid):
	json = _getUrbanJSON(UD_DEFID_URL + urlquote(str(defid)))
	return _parseUrbanJSON(json)

def random():
	json = _getUrbanJSON(UD_RANDOM_URL)
	return _parseUrbanJSON(json, False)