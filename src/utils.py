def get_if_possible(element, json):
	try:
		keys = element.split('.')
		rv = json
		for key in keys:
			rv = rv[key]
		return rv

	except KeyError:
		return None
	except TypeError:
		return None	
