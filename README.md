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

d = Dependabot("TOKEN", "https://api.github.com/graphql")
depedanbot_alerts = d.get_security_alerts(auth_token='or-elias', graphql_endpoint='pyDependabot')

print(depedanbot_alerts)
```


