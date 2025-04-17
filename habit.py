from helper import *
from datetime import datetime, timedelta

WEEKDAYS = "MTWTFSS"


class Habit:
	def __init__(self, title: str):
		self.title = title
		self.data = self.load()
		self.update_stats()

	def update_stats(self):
		yesterday = datetime.today() + timedelta(days=1)
		streak = 0
		while True:
			yesterday = yesterday - timedelta(days=1)

			if yesterday.strftime('%Y-%m-%d') in self.data['logs'].keys():
				streak += 1
			else:
				break
		
		self.data['streak'] = streak

	def get_maxima(self):
		maximum = -float("inf")
		minimum = float("inf")
		for key, value in self.data['logs'].items():
			if value > maximum:
				maximum = value
			elif value < minimum:
				minimum = value

		return {
			"maximum": maximum,
			"minimum": minimum
		}


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
				string_date = current_date.strftime('%Y-%m-%d')
				if string_date in week:
					if self.get_plurality():
						print(get_square(self.get_maxima(), self.data['logs'][string_date]), end="")
					else:
						print("■", end="")
					# pick gradient here ▤▦▩■

				else:
					print("□", end="")

				current_date = current_date + timedelta(weeks=1)

			print("")

		print("\n streak:", self.data['streak'])
		if self.data['is_plural']:
			print(" average:", round(self.data['average'], 2))

	def get_plurality(self):
		return self.data["is_plural"]

	def save(self):
		all_data = get_habits_json()
		all_data[self.title] = self.data
		save_habits_json(all_data) 

	def load(self):
		return get_habits_json()[self.title]

	def log(self, amount):
		self.log_previous(amount, datetime.today().strftime('%Y-%m-%d'))

	def log_previous(self, amount, date):
		self.update_stats()

		self.data['average'] = (self.data['average'] * len(self.data['logs']) + amount) / (len(self.data['logs']) + 1)
		self.data['logs'][date] = amount

		self.save()

	def update(self):
		pass

