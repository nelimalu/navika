from constants import *
from helper import *


def handle_view(args):
	if len(args) == 0:
		log_syntax_error(VIEW_SYNTAX_MSG)
		return

	# todo print calendar
	# load in gym object from file
	# create class object from file
	# print calendar
	pass


def handle_list():
	print(LIST_MSG)
	for i, title in enumerate(get_habits_list()):
		print(f"  {i + 1}. {title.upper()}")


def handle_log(args):
	if len(args) == 0:
		log_syntax_error(LOG_SYNTAX_MSG)
		return

	# send command to object in argument
	pass


def handle_help():
	print(HELP_MSG)
	for i, syntax in enumerate(SYNTAX_LIST):
		print(f"  {i + 1}. {syntax}")


def handle_create(args):
	if len(args) == 0:
		log_syntax_error(CREATE_SYNTAX_MSG)
		return

	habit = args[0]
	habits_list = get_habits_list()

	if habit in habits_list:
		log_error(f"A habit with name '{habit}' already exists!")
		return




def handle_delete(args):
	if len(args) == 0:
		log_syntax_error(DELETE_SYNTAX_MSG)
		return

	habit = args[0]
	habits_list = get_habits_list()

	if habit not in habits_list:
		log_error(f"No habit with name '{habit}' exists!")
		return

	query_yn("Are you sure you want to delete this habit?", preference="N")




def handle_not_found():
	print(NOT_FOUND_MSG)
	
