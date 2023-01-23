from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from pyDependabot.repository_vulnerablity_alert_query import RepositoryVulnerablityAlertQuery
from pyDependabot.repository_vulnerablity_alert_node import RepositoryVulnerablityAlert


class Dependabot():
	def __init__(self, auth_token, graphql_endpoint, print_debug_log=False):
		self.debug = print_debug_log
		transport = RequestsHTTPTransport( url=graphql_endpoint, headers = {"Authorization": f"bearer {auth_token}"} )
		self.client = Client(transport=transport)
		print(f"Successfully created a graphql client") if self.debug is True else None


	def get_security_alerts(self, repository_owner: str, repository_name: str,
							fields=[RepositoryVulnerablityAlertQuery.securityVulnerabilityField, RepositoryVulnerablityAlertQuery.createdAtField]):

		# for more information please read the official docs - https://github.com/or-elias/pyDependabot
		#
		# Input parameters:
		#	- repository_owner - sometimes refered to as the organization of the repository. i.e. microsoft
		#   - repository_name - the full name of the repo. i.e. vscode
		#   - fields - not mandatory. a list of consts from RepositoryVulnerablityAlertQuery class. represents the data we ask from the server.
		# 
		# Output - 
		#	for now the function returns a list of raw nodes as returned from the server. 
		#	also, if we received a graphql error from github (for example, NOT FOUND), we let the gql.transport.exceptions.TransportQueryError excption to be raised.
		#
		if len(fields) == 0:
			raise Exception("GraphQL query must fetch at least one field. Got empty list of fields")
		raw_nodes_from_dependabot = self._query_api_for_repositories_vulnerablities(repository_owner, repository_name, fields)
		return [RepositoryVulnerablityAlert(node, repository_owner, repository_name) for node in raw_nodes_from_dependabot]
		



	def _query_api_for_repositories_vulnerablities(self, repository_owner, repository_name, fields, after=None, current_results=[]) -> list[dict]:
		# A recursive function that returns a list of raw nodes representing vulnerablities alerts from github.
		# A node is a github graphql object as shown here https://docs.github.com/en/graphql/reference/interfaces#node. we fetch it's RepositoryVulnerability fields.
		# Note: This function doesnt have recursive depth limitation since we figured a single repository will probably wont have thousands of alerts.
		#

		q = f"""
			query GetRepositoryDependabotAlerts ($name: String!, $owner: String!, $after: String) {{ 
					repository( name: $name, owner: $owner) {{
																 
						vulnerabilityAlerts(first: 99, after: $after) {{  
							pageInfo {{ hasNextPage, endCursor }} ,
							nodes{{ {','.join(fields)} }} 
						}}
					}} 	
			}}
		"""
		vars = {"name": repository_name, "owner":repository_owner, "after": after}
		results = self.client.execute(gql(q), variable_values=vars)
		
		# Because of the nature of Graphql, I can be sure that I will always get 'endCursor' and 'node' fields in the response, even if they are empty.
		end_cursor = results.get('repository').get('vulnerabilityAlerts').get('pageInfo').get('endCursor')
		nodes = results.get('repository').get('vulnerabilityAlerts').get('nodes')
		
		if end_cursor is None:
			return current_results+nodes
		else:
			return self._query_api_for_repositories_vulnerablities(repository_owner, repository_name, fields, after=end_cursor, current_results=current_results+nodes)

