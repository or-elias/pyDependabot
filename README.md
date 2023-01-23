# pyDependabot
 The unofficial but well maintained python library to interact with github's Depedabot api

## What is it? 


## installation 
Currently installtion is manual.
Follow these steps to install pyDependabot successfully.

- clone the repository to your local machine
- cd into the folder
- run 'python setup.py' install

after that the package will be avaiable for usage.
if you encounter any problem during installtion, please open an issue in our github and we will help.

## Usage examples
Please note that in order to use the package the token you authenticate with must have security alerts permissions.

To simply query your current Dependabot alert - 

```python

import Dependabot from pyDependabot 

d = Dependabot(auth_token="TOKEN",  graphql_endpoint="https://api.github.com/graphql")
depedanbot_alerts = d.get_security_alerts(repository_owner='or-elias',repository_name='pyDependabot')

print(depedanbot_alerts)
```

If you need to query different fields you can specify that on the get_security_alerts function call.
All of the the possible fields are listed on the repository_vulnerablity_alert_query.py file
```python

import Dependabot from pyDependabot 
from pyDependabot.repository_vulnerablity_alert_query import RepositoryVulnerablityAlertQuery

d = Dependabot(auth_token="TOKEN",  graphql_endpoint="https://api.github.com/graphql")
depedanbot_alerts = d.get_security_alerts(repository_owner='or-elias',repository_name='pyDependabot', fields=[RepositoryVulnerablityAlertQuery.dismissCommentField])

print(depedanbot_alerts)
```


