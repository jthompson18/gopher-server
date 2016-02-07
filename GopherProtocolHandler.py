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
			'text': '8070',
			'type': 'dir',
			'files': ['Test File Three', 'Test File Four']
			}
			]
			self.query_results = []

		def get_file(self, res_name):
			filename = "%s.txt" %res_name.replace(' ', '').lower() 
			o = open(filename, 'r')
			lines = o.readlines()
			lines.append('\n.')
			o.close()
			return lines

		def resolve_gquery(self, query):
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
			if len(self.query_results) > 0 and type(self.query_results) is str:
				for res in self.query_results:
					restext = "{0}{1} \t {2}{3}".format(res['name'], res['selector'], res['host'], res['port'])
					results.append("{0}{1}{2} \r\n".format(self.prefixes[res['type']], restext, self.sufix))
				results.append(".")
			elif type(self.query_results) is list:
				results = self.query_results
			else:
				results.append("\t\t\tFILE NOT FOUND\t\t\t \r\n")
				results.append(".")

			return ''.join(results)