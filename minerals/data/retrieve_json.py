import json
import re

def pull_json(file):
	with open(file, 'r') as json_file:
		data = json.load(json_file)

	return data