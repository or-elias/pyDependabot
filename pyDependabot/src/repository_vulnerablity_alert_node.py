from datetime import datetime
from packaging import version

from .utils import get_if_possible
from .consts import NOT_POPULATED


class securityVulnerability(object):
	def __init__(self):
		# we list here the properties of security vulnerability for autocompletion in IDE. that's the only reason.
		self.severity = None
		self.first_patched_version = None
		self.package_ecosystem = None
		self.package_name = None
		self.updated_at = None
		self.vulnerable_version_range = None
		self.advisory_summary = None
		self.advisory_cvss_score = None

class Dismisser(object):
	def __init__(self):
		# we list here the properties of security vulnerability for autocompletion in IDE. that's the only reason.
		self.email = None
		self.name = None
		self.login = None
		self.url = None
		return 


class RepositoryVulnerablityAlert(object):
	def __init__(self, node, repository_owner, repository_name):
		self.node = node
		self.repository_owner = repository_owner
		self.repository_name = repository_name

	@property
	def securityVulnerability(self):
		security_vulnerability = securityVulnerability()
		security_vulnerability.severity = get_if_possible(self.node, "securityVulnerability.severity")
		security_vulnerability.package_ecosystem = get_if_possible(self.node, "securityVulnerability.package.ecosystem")
		security_vulnerability.package_name = get_if_possible(self.node, "securityVulnerability.package.name")
		security_vulnerability.vulnerable_version_range = get_if_possible(self.node, "securityVulnerability.vulnerableVersionRange")
		security_vulnerability.advisory_cvss_score = get_if_possible(self.node, "securityVulnerability.advisory.cvss.score")
		security_vulnerability.advisory_summary = get_if_possible(self.node, "securityVulnerability.advisory.summary")
		
		first_patched_version = get_if_possible(self.node, "securityVulnerability.firstPatchedVersion.identifier") 
		security_vulnerability.first_patched_version = version.parse(first_patched_version) if first_patched_version is not NOT_POPULATED else NOT_POPULATED
		
		updated_at = get_if_possible(self.node, "securityVulnerability.updatedAt") 
		security_vulnerability.updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ") if updated_at is not NOT_POPULATED else NOT_POPULATED
		
		return security_vulnerability

	@property
	def createdAt(self):
		createdAt = self.node.get("createdAt")
		return datetime.strptime(createdAt, "%Y-%m-%dT%H:%M:%SZ") if createdAt is not NOT_POPULATED else NOT_POPULATED
		
	@property
	def dismissedAt(self):
		dismissedAt = self.node.get("dismissedAt")
		return datetime.strptime(dismissedAt, "%Y-%m-%dT%H:%M:%SZ") if dismissedAt is not NOT_POPULATED else NOT_POPULATED

	@property
	def dismisser(self):
		dismisser = Dismisser()
		dismisser.name = get_if_possible(self.node, "dismisser.name")
		dismisser.login = get_if_possible(self.node, "dismisser.login")
		dismisser.email = get_if_possible(self.node, "dismisser.email")
		dismisser.url = get_if_possible(self.node, "dismisser.url")
		return dismisser

	
	@property
	def state(self):
		return self.node.get("state")
		
	@property
	def vulnerable_manifest_path(self):
		return self.node.get("vulnerableManifestPath")
		

	@property
	def vulnerable_requirements(self):
		return self.node.get("vulnerableRequirements")

	@property
	def vulnerable_manifest_filename(self):
		return self.node.get("vulnerableManifestFilename")

	@property
	def dismiss_comment(self):
		return self.node.get("dismissComment")

	@property
	def dismiss_reason(self):
		print(self.node)
		return self.node.get("dismissReason")
	
	@property
	def fixed_at(self):
		return self.node.get("fixedAtField")
	
	@property
	def number(self):
		return self.node.get("number")
	
	def __repr__(self):
		return f"""(Repository:{self.repository_owner}/{self.repository_name}, Package:{self.securityVulnerability.package_name}:{self.securityVulnerability.severity}-severity)"""