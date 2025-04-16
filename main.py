from constants import *
from handler import *
from helper import * 
import json

'''
squares:
□▤▦▩■

make info command, with date param
prints all logs on that day with values
'''


def startup():
	# loop all data and update

	print(STARTUP_MSG)
	list()


def query():
	request = input("\n>").lower().split()
	command = request[0]
	args = request[1:]

	if command == "list":
		handle_list()
	elif command == "view":
		handle_view(args)
	elif command == "log":
		handle_log(args)
	elif command == "help":
		handle_help()
	elif command == "create":
		handle_create(args)
	elif command == "delete":
		handle_delete(args)
	elif command == "quit":
		return False
	else:
		handle_not_found()

	return True


def main():
	startup()

	run = True
	while run:
		run = query()


if __name__ == "__main__":
	main()
