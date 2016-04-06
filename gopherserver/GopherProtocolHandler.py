import os

class GopherProtocolHandler:
		def __init__(self):
			self.prefixes = {
			'file': '0',
			'dir': '1',
			'cso-phone': '2',
			'err': '3',
			'bin-hexed-mac': '4',
			'dos-bin': '5',
			'unix': '6',
			'isearch-serv': '7',
			'telnet': '8',
			'bin': '9'
			}

			self.isFile = False

			self.sufix = "\r\n"

			self.test_server_results=[
			{
			'name': 'Test File One',
			'selector': 'getFileOne',
			'host': 'localhost',
			'port': '8070',
			'type': 'file'
			},
			{
			'name': 'Test File Two',
			'selector': 'getFileTwo',
			'host': 'localhost',
			'port': '8070',
			'type': 'file'
			},
			{
			'name': 'Test File Three',
			'selector': 'getFileThree',
			'host': 'localhost',
			'port': '8070',
			'type': 'file'
			},
			{
			'name': 'Test File Four',
			'selector': 'getFileFour',
			'host': 'localhost',
			'port': '8070',
			'type': 'file'
			},
			{
			'name': 'Test Dir One',
			'selector': '/DirOne',
			'host': 'localhost',
			'port': '8070',
			'type': 'dir',
			'files': ['Test File One']
			},
			{
			'name': 'Test Dir Two',
			'selector': '/DirTwo',
			'host': 'localhost',
			'port': '8070',
			'type': 'dir',
			'files': ['Test File Two']
			},
			{
			'name': 'Test Dir Three',
			'selector': '/DirThree',
			'host': 'localhost',
			'port': '8070',
			'type': 'dir',
			'files': ['Test File Three', 'Test File Four']
			}
			]
			self.query_results = []

		def get_file(self, res_name):
			self.isFile = True
			filename = "/testfiles/%s.txt" %res_name.replace(' ', '').lower()
			cwd = os.getcwd()
			
			print(cwd+filename)
			o = open(cwd+filename, 'r')
			lines = o.readlines()
			lines.append('\n.')
			o.close()
			return lines

		def resolve_gquery(self, query):
			self.query = query
			if query != ' ':
				if query.startswith('/'):
					files = []
					for res in self.test_server_results:
						if query == res['selector']:
							files = res['files']
					for res in self.test_server_results:
						if res['name'] in files:
							self.query_results.append(res)
				else:
					for res in self.test_server_results:
						if query == res['selector']:
							self.query_results = self.get_file(res['name'])
							break
			else:
				self.query_results = self.test_server_results


		def get_result_strings(self):
			results = []
			if self.isFile:
				results = self.query_results
			elif len(self.query_results) > 0:
				for res in self.query_results:
					restext = "{0}{1} \t {2}{3}".format(res['name'], res['selector'], res['host'], res['port'])
					results.append("{0}{1}{2}".format(self.prefixes[res['type']], restext, self.sufix))
				results.append(".")
			else:
				results.append("\t\t\tFILE NOT FOUND\t\t\t \r\n")
				results.append(".")
			r = ''
			for res in results:
				if type(res) is str:
					r+= res
			return r

			