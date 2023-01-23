from datetime import datetime
from packaging import version

from pyDependabot.utils import get_if_possible


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



class RepositoryVulnerablityAlert(object):
	def __init__(self, node, repository_owner, repository_name):
		self.node = node
		self.repository_owner = repository_owner
		self.repository_name = repository_name

	@property
	def securityVulnerability(self):
		security_vulnerability = securityVulnerability()
		security_vulnerability.severity = get_if_possible("securityVulnerability.severity", self.node)
		security_vulnerability.package_ecosystem = get_if_possible("securityVulnerability.package.ecosystem", self.node)
		security_vulnerability.package_name = get_if_possible("securityVulnerability.package.name", self.node)
		security_vulnerability.vulnerable_version_range = get_if_possible("securityVulnerability.vulnerableVersionRange", self.node)
		security_vulnerability.advisory_cvss_score = get_if_possible("securityVulnerability.advisory.cvss.score", self.node)
		security_vulnerability.advisory_summary = get_if_possible("securityVulnerability.advisory.summary", self.node)
		
		first_patched_version = get_if_possible("securityVulnerability.firstPatchedVersion.identifier", self.node) 
		security_vulnerability.first_patched_version = version.parse(first_patched_version) if first_patched_version is not None else None
		
		updated_at = get_if_possible("securityVulnerability.updatedAt", self.node) 
		security_vulnerability.updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%SZ") if updated_at is not None else None
		
		return security_vulnerability

	@property
	def createdAt(self):
		createdAt = self.node.get("createdAt")
		return datetime.strptime(createdAt, "%Y-%m-%dT%H:%M:%SZ") if createdAt is not None else None
		
	@property
	def dismissedAt(self):
		dismissedAt = self.node.get("dismissedAt")
		return datetime.strptime(dismissedAt, "%Y-%m-%dT%H:%M:%SZ") if dismissedAt is not None else None

	@property
	def dismisser(self):
		dismisser = Dismisser()
		dismisser.name = get_if_possible("dismisser.name", self.node)
		dismisser.login = get_if_possible("dismisser.login", self.node)
		dismisser.email = get_if_possible("dismisser.email", self.node)
		dismisser.url = get_if_possible("dismisser.url", self.node)
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