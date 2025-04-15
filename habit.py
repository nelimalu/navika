from helper import *


class Habit:
	def __init__(self, title: str):
		self.title = title
		self.data = self.load()

	def view(self):
		pass

	def save(self):
		pass

	def load(self):
		return get_habits_json()[self.name]

	def log(self, amount):
		pass

	def update(self):
		pass
