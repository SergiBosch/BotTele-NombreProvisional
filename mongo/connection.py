from pymongo import MongoClient

class MongoConnection:

	def __init__(self, data_base, collection):
		self.client = MongoClient('localhost', 27017)
		self.data_base = self.client[data_base]
		self.collection = self.data_base[collection]