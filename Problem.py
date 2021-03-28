

class Street:
	def __init__(self, idx, begin, end, name, length):
		self.idx = idx
		self.begin = int(begin)
		self.end = int(end)
		self.name = name
		self.length = int(length)

	def __eq__(self, other):
		return self.idx == other.idx

	def __hash__(self):
		return self.idx


class Problem:

	def __init__(self):
		self.duration = 0
		self.nb_inter = 0
		self.nb_streets = 0
		self.nb_cars = 0
		self.bonus = 0

		self.streets = set()
		self.useful_streets = set()
		self.cars = []

	def parse_from_stream(self, stream):
		# header
		split = stream.readline().strip().split()
		self.duration, self.nb_inter, self.nb_streets, self.nb_cars, self.bonus = map(int, split)
		
		# streets
		streets = []
		for idx in range(self.nb_streets):
			sp = stream.readline().strip().split()
			streets.append(Street(idx, *sp))
		
		# cars
		used_streets = []
		for idx in range(self.nb_cars):
			sp = stream.readline().strip().split()[1:]
			self.cars.append(sp)

			used_streets.extend(sp)

		#remove unused streets
		used_streets = frozenset(used_streets)
		streets = [s for s in streets if s.name in used_streets]
		print(self.nb_streets, len(streets))
		self.streets = frozenset(streets)

