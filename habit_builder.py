import datetime
import json


class HabitBuilder:
	def __init__(self, title: str, subtitle: str, is_plural: bool):
		self.title = title
		self.subtitle = subtitle
		self.is_plural = is_plural
		self.raw_json = generate_json()

	def generate_json(self):
		return {
			"title": self.name
			"subtitle": self.subtitle,
			"streak": 0,
			"average": 0.0,
			"is_plural": self.is_plural,
			"logs": {}
		}

	def save(self):
		with open('data.json', 'r') as file:
			data = json.load(file)

		if self.title not in data.keys():
			data[self.title] = self.raw_json

		with open('data.json', 'w') as file:
			json.dump(data, file)
