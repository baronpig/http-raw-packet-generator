from urlparse import urlparse
from socket import socket

class HRPG(object):

	def __init__(self):
		self.url = None
		self.method = None
		self.headers = {}
		return

	def set_url(self, url):
		self.url = url

	def set_method(self, method):
		self.method = method

	def set_headers(self, *args):
		# todo: support tuple
		len_args = len(args)

		if len_args == 1 and \
		(type(args[0]) == dict or\
		 type(args[0]) == tuple):
			self.headers.update(args[0])
		elif len_args == 2:
			self.headers[args[0]] = args[1]
		else:
			print("""set_headers(dict)
				set_headers(tuple)
				set_headers(str, str)""")

		return

	def generate_raw_packet(self):
		try:
			parsed = urlparse(self.url)
		except:
			print ("set url first")
			return

		payload = """%s %s HTTP/1.1
Host: %s""" % (self.method, self.url, parsed.netloc)

		for header in self.headers.keys():
			value = self.headers[header]
			payload += "\n%s: %s" % (header, value)

		payload = payload.replace("\n", "\r\n")

		print (payload)

		return payload
