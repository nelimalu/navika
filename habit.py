import json


class Habit:
	def __init__(self, title: str):
		self.title = title
		self.data = self.load()

	def view(self):
		pass

	def save(self):
		pass

	def load(self):
		with open('data.json', 'r') as file:
			data = json.load(file)[self.name]
		return data

	def log(self, amount):
		pass

	def update(self):
		pass
