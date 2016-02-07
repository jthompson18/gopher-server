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
			# {
			# 'name': 'Test Dir One',
			# 'selector': 'getDirOne',
			# 'host': 'localhost',
			# 'port': '8070',
			# 'type': 'dir'
			# },
			# {
			# 'name': 'Test Dir Two',
			# 'selector': 'getDirTwo',
			# 'host': 'localhost',
			# 'port': '8070',
			# 'type': 'dir'
			# },
			# {
			# 'name': 'Test Dir Three',
			# 'selector': 'getDirTwo',
			# 'host': 'localhost',
			# 'text': '8070',
			# 'type': 'dir'
			# }
			]
			self.query_results = []

		def resolve_gquery(self, query):
			if query != ' ':
				for res in self.test_server_results:
					if query is res['selector']:
						self.query_results.append(res)
						break
			else:
				self.query_results = self.test_server_results


		def get_result_strings(self):
			results = []
			if len(self.query_results) > 0:
				for res in self.query_results:
					restext = "{0}{1} \t {2}{3}".format(res['name'], res['selector'], res['host'], res['port'])
					results.append("{0}{1}{2} \r\n".format(self.prefixes[res['type']], restext, self.sufix))
			else:
				results.append("\t\t\tFILE NOT FOUND\t\t\t \r\n")
			results.append(".")

			return ''.join(results)