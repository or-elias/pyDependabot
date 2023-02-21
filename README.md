# pyDependabot
The unofficial but well maintained python library to interact with github's Dependabot api.
pydependabot allows developers to work with github's vulnerablity alerts without handling graphql or rest api, just by using python.

## installation 
Pip is the easiest way to install pydependabot.
```
python -m pip install pydependabot
```

after a short installation process the package will be avaiable for usage.
if you encounter any problem during installation, please open an issue and we will help.

## Usage examples
Please note that in order to use the package the token you authenticate with must have security alerts permissions.

To simply query your current Dependabot alerts list - 

```python

import Dependabot from pydependabot 

d = Dependabot(graphql_endpoint="https://api.github.com/graphql", auth_token="TOKEN")
dependabot_alerts = d.get_security_alerts(repository_owner='or-elias',repository_name='pyDependabot')

print(dependabot_alerts)
```

If you need to query different fields you can specify that on the get_security_alerts function call.
All of the possible fields are listed on the repository_vulnerablity_alert_query.py file
```python

import Dependabot from pydependabot 
from pydependabot.repository_vulnerablity_alert_query import RepositoryVulnerablityAlertQuery

d = Dependabot(graphql_endpoint="https://api.github.com/graphql", auth_token="TOKEN")
dependabot_alerts = d.get_security_alerts(repository_owner='or-elias',repository_name='pyDependabot', fields=[RepositoryVulnerablityAlertQuery.dismissCommentField])

print(dependabot_alerts)
```


pydependabot uses a gql client to ineract with the graphql endpoint and it automatically selects RequestsHTTPTransport as the client's transport method.
if needed, you can manully overwrite that and provide your own gql client for the library to use, you can do that by using the options argument.

```python

import Dependabot from pydependabot 

client = ADifferentGQLClient()
dependabot_alerts = Dependabot("https://api.github.com/graphql", "TOKEN", options={'client': client}).get_security_alerts('fake-org', 'fake-repo')
print(dependabot_alerts)

```