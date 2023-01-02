from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport



class RepositoryVulnerablityAlertQuery(object):
	createdAtField = "createdAt"
	securityVulnerabilityField = " securityVulnerability { severity }  "
	dismissedAtField = "dismissedAt"





class Dependabot():
	def __init__(self, auth_token, graphql_endpoint):
		transport = RequestsHTTPTransport( url=graphql_endpoint, headers = {"Authorization": f"bearer {auth_token}"} )
		self.client = Client(transport=transport)


	def get_vulnerablties_of_repository(self,
										repository_owner,
										repository_name,
										fields=[RepositoryVulnerablityAlertQuery.securityVulnerabilityField,
											    RepositoryVulnerablityAlertQuery.createdAtField]):
		
		query = gql(self.build_query_to_fetch_vulnerablities(repository_owner, repository_name, fields))
		results = self.client.execute(query)
		print(results)
		




	def build_query_to_fetch_vulnerablities(self, repository_owner, repository_name, fields):
		return f"""
					{{ 
						repository( name: "{repository_name}", owner: "{repository_owner}") {{
						 																		vulnerabilityAlerts(first: 10) {{  nodes{{ {','.join(fields)} }} }}
																							}} 
					}}
				"""
			
