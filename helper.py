import json
from getch import getch
import time


def get_habits_list():
	with open('data.json', 'r') as file:
		data = json.load(file).keys()
	return data


def log_syntax_error(error):
	print(SYNTAX_ERROR_MSG + error)


def log_error(error):
	print(ERROR_MSG + error)


def query_yn(message, preference="Y"):
	#while True:
	query_prompt = "[Y/n]" if preference == "Y" else "[y/N]"
	print(message, query_prompt, end=" ")
	time.sleep(0.1)

	response = getch()
	str_response = response.decode()

	if response == b'\r':
		str_response = preference

	if response.upper() == 'Y':
		return True
	elif response.upper() == 'N':
		return False


if __name__ == "__main__":
	print(query_yn("balls?", preference="Y"))
