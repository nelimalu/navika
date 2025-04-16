from helper import *
from datetime import datetime, timedelta

WEEKDAYS = "MTWTFSS"


class Habit:
	def __init__(self, title: str):
		self.title = title
		self.data = self.load()

	def view(self):
		logs = [[] for _ in range(7)]
		today = datetime.today()

		# 21  -  27
		message = f"-- {self.title.upper()} --"
		# 56 long
		print("\n", " " * ((56 // 2) - (len(message) // 2) - 1), message)

		print("\n   ", end="")

		for str_date, value in self.data['logs'].items():
			date = datetime.strptime(str(str_date), "%Y-%m-%d")
			logs[date.weekday()].append(date.strftime('%Y-%m-%d'))

		'''
	
		USE THIS FOR TESTING

		current_date = today - timedelta(weeks=53)
		current_month = current_date.strftime("%b").upper()
		print("\n   ", end="")
		for i in range(53):
			current_date = current_date + timedelta(weeks=1)
			new_month = current_date.strftime("%b").upper()
			print(new_month[0], end="")

		print("\n   ", end="")
		'''

		# print months on top
		current_date = today - timedelta(weeks=53)
		current_month = current_date.strftime("%b").upper()
		prev_month = ""

		unique = 0
		i = 0
		while i <= 52:
			current_date = current_date + timedelta(weeks=1)
			new_month = current_date.strftime("%b").upper()

			if new_month != prev_month:
				prev_month = new_month
				unique += 1
				if unique == 2:
					unique = 0
					print(new_month[:3], end="")
					current_date = current_date + timedelta(weeks=2)
					i += 3
					continue
			
			print(" ", end="")

			i += 1

		print()

		# print calendar
		for x, week in enumerate(logs):
			print(f" {WEEKDAYS[x]} ", end="")
			# print(week)

			delta = timedelta(days=(today.weekday() - x))
			start_date = today - delta

			current_date = start_date - timedelta(weeks=52)
			for past_week in range(53 if x <= today.weekday() else 52):
				# print(current_date.strftime('%Y-%m-%d'))
				if current_date.strftime('%Y-%m-%d') in week:
					print("■", end="")
				else:
					print("□", end="")

				current_date = current_date + timedelta(weeks=1)

			print("")

		print("\n streak:", self.data['streak'])
		print(" average:", self.data['average'])

	def getPlurality(self):
		return self.data["is_plural"]

	def save(self):
		all_data = get_habits_json()
		all_data[title] = self.data
		save_habits_json(all_data) 

	def load(self):
		return get_habits_json()[self.title]

	def log(self, amount):
		pass

	def log_previous(self, amount, date):
		pass

	def update(self):
		pass

