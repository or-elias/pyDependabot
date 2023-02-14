# dissmiseedattt value is populated correcly, etc
# all datetime objects are datetime
# all sub values (like dismisser.name) are populated correctly
# missing values are populated with NOT_POPULATED

import sys; sys.path.append("..")
from pyDependabot.src.repository_vulnerablity_alert_node import RepositoryVulnerablityAlert

import datetime


def test_created_at_returns_datetime_type():
	mock = {'createdAt': '2022-06-15T19:10:06Z'}	
	assert isinstance(RepositoryVulnerablityAlert(mock, "fake-repo-owner", "fake-repo-name").created_at, datetime.datetime)



def test_dismissed_at_returns_datetime_type():
	mock = {'dismissedAt': '2022-06-15T19:10:06Z'}	
	assert isinstance(RepositoryVulnerablityAlert(mock, "fake-repo-owner", "fake-repo-name").dismissed_at, datetime.datetime)


def test_security_vulnerability_updated_at_returns_datetime_type():
	mock = {'securityVulnerability': {'advisory': {'cvss': {'score': 4.3},'summary': 'Misinterpretation of malicious XML input'},   
                           			  'firstPatchedVersion': {'identifier': '0.5.0'},   
                           			  'package': {'ecosystem': 'NPM', 'name': 'xmldom'},
                           			  'severity': 'MODERATE',
                           			  'updatedAt': '2021-08-25T00:31:47Z',
                           			  'vulnerableVersionRange': '< 0.5.0'}}

	assert isinstance(RepositoryVulnerablityAlert(mock, "fake-repo-owner", "fake-repo-name").securityVulnerability.updated_at, datetime.datetime)

	
def test_fixed_at_returns_datetime_type():
	mock = { "fixedAt": '2022-06-15T19:10:06Z' }
	assert isinstance(RepositoryVulnerablityAlert(mock, "fake-repo-owner", "fake-repo-name").fixed_at, datetime.datetime)

