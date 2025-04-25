import json
from readchar import readchar
import time
from constants import *


def get_habits_list():
	with open(FILEPATH, 'r') as file:
		data = json.load(file).keys()
	return data


def log_syntax_error(error):
	print(SYNTAX_ERROR_MSG + error)


def log_error(error):
	print(ERROR_MSG + error)


def get_habits_json():
	with open(FILEPATH, 'r') as file:
		return json.load(file)


def save_habits_json(data):
	with open(FILEPATH, 'w') as file:
		json.dump(data, file, indent=4)


def query_yn(message, preference="Y"):
	while True:
		query_prompt = "[Y/n]" if preference == "Y" else "[y/N]"
		print(message, query_prompt, end=" ", flush=True)

		response = readchar()
		byte_response = response.encode()

		if byte_response == b'\r':
			response = preference

		if response.upper() == 'Y':
			return True
		elif response.upper() == 'N':
			return False

		print("\n", flush=True)


def colour(text, c=COLOUR):
	return f"{c}{text}\033[00m"


def get_square(maxima, value):
	maximum = maxima['maximum']
	minimum = maxima['minimum']

	if maximum - minimum == 0:
		return colour('■')

	percentage = (value - minimum) / (maximum - minimum)
	# ▤▦▩■

	if percentage < 0.25:
		return colour('▤')
	elif percentage < 0.5:
		return colour('▦')
	elif percentage < 0.75:
		return colour('▩')
	return colour('■')



if __name__ == "__main__":
	#print(readchar().encode())
	print(query_yn("balls?", preference="Y"))
