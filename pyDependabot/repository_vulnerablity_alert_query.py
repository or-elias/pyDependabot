

class RepositoryVulnerablityAlertQuery(object):
	createdAtField = "createdAt"
	securityVulnerabilityField = """ securityVulnerability { 
										severity,
										firstPatchedVersion  { identifier  },
										package { ecosystem, name },
										updatedAt,
									    vulnerableVersionRange,
										advisory { summary, cvss { score } }, 
									}  """

	dismissedAtField = "dismissedAt"
	dismissCommentField = "dismissComment"
	dismissReasonField = "dismissReason"
	dismisserField = "dismisser { email, name, login, url }" # requires  ['user:email', 'read:user'] permissions
	fixedAtField = "fixedAt"
	numberField = "number"
	stateField = "state"
	vulnerableManifestFilenameField = "vulnerableManifestFilename"
	vulnerableManifestPathField = "vulnerableManifestPath"
	vulnerableRequirementsField =  "vulnerableRequirements"

