import json
from readchar import readchar
import time


def get_habits_list():
	with open('data.json', 'r') as file:
		data = json.load(file).keys()
	return data


def log_syntax_error(error):
	print(SYNTAX_ERROR_MSG + error)


def log_error(error):
	print(ERROR_MSG + error)


def get_habits_json():
	with open('data.json', 'r') as file:
		return json.load(file)


def save_habits_json(data):
	with open('data.json', 'w') as file:
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


if __name__ == "__main__":
	#print(readchar().encode())
	print(query_yn("balls?", preference="Y"))
