from constants import *
from helper import *
from habit import Habit


def handle_view(args):
	if len(args) == 0:
		log_syntax_error(VIEW_SYNTAX_MSG)
		return

	habit = args[0]
	habits_list = get_habits_list()

	if habit not in habits_list:
		log_error(f"No habit with name '{habit}' exists!")
		return

	habit_object = Habit(habit)

	habit_object.view()


def handle_week():
	habits_json = get_habits_json()
	habits_list = get_habits_list()
	longest_habit = max([len(x) for x in habits_list])

	print("")
	print(" " * longest_habit, "MTWTFSS")

	for habit, data in habits_json.items():
		print((" " * (longest_habit - len(habit))) + habit, end=" ")

		habit_object = Habit(habit)
		habit_object.view_week()


def handle_list():
	print(LIST_MSG)
	for i, title in enumerate(get_habits_list()):
		print(f"  {i + 1}. {title.upper()}")


def handle_log(args):
	if len(args) < 1 or len(args) > 3:
		log_syntax_error(LOG_SYNTAX_MSG)
		return
	
	habits_list = get_habits_list()
	habit = args[0]

	if habit not in habits_list:
		log_error(f"No habit with name '{habit}' exists!")
		return

	habit_object = Habit(habit)

	if habit_object.get_plurality():
		if len(args) == 2:
			habit_object.log(float(args[1]))
		if len(args) == 3:
			habit_object.log_previous(float(args[1]), args[2])
	else:
		if len(args) == 1:
			habit_object.log(1)
		if len(args) == 2:
			habit_object.log_previous(1, args[1])

	print(f"\n Successfully logged your habit.")
	handle_view([habit])


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

	plurality = query_yn("Should your habit log a range (plurality) of values?", preference="Y")

	habits = get_habits_json()
	habits[habit] = {
		"title": args[0],
		"streak": 0,
		"average": 0.0,
		"is_plural": plurality,
		"logs": {}
	}
	save_habits_json(habits)

	print(f"\nSuccessfully created habit '{habit}'")


def handle_delete(args):
	if len(args) == 0:
		log_syntax_error(DELETE_SYNTAX_MSG)
		return

	habit = args[0]
	habits_list = get_habits_list()

	if habit not in habits_list:
		log_error(f"No habit with name '{habit}' exists!")
		return

	if not query_yn("Are you sure you want to delete this habit?", preference="N"):
		return

	habits = get_habits_json()
	del habits[habit]
	save_habits_json(habits)

	print(f"\nSuccessfully deleted habit '{habit}'")


def handle_not_found():
	print(NOT_FOUND_MSG)


def handle_info(args):
	if len(args) == 0:
		log_syntax_error(INFO_SYNTAX_MSG)
		return

	date = args[0]
	print(f"\n Here is everything logged on {date}:")

	data = get_habits_json()
	for habit, info in data.items():
		if date in info['logs'].keys():
			print(f"  {habit}: {info['logs'][date]}")


def handle_viewall():
	habits_json = get_habits_json()

	for habit, data in habits_json.items():
		habit_object = Habit(habit)
		habit_object.view()
	
