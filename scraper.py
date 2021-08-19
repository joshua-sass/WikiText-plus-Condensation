from storage import storage

class scraper:
	def __init__(self):
		print("scraper initialized...")

		#https://www.gamepedia.com/wikis
		#https://en.wikipedia.org/wiki/List_of_wikis

		#scraper above links to generate database, always do on program launch but allow multiple questions
		#selenium magic here

		self.store = storage()

	def query(self, location, quer):
		self.store.query(location, quer)