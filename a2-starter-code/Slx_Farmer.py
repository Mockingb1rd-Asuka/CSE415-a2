SOLUZION_VERSION = "1.0"
PROBLEM_NAME = "Farmer and Fox"
PROBLEM_VERSION = "1.0"
PROBLEM_AUTHORS = ['Lingxuan Shi']
PROBLEM_CREATION_DATE = "Oct-08-2019"
PROBLEM_DESC=\
'''Farmer_Fox.py
by Lingxuan Shi
UWNetID: LS64
Student number: 1663139 '''

LEFT = 0
RIGHT = 1
Farmer = 0
Fox = 1
Chicken = 2
Grain = 3
nameofpassengers = ['Farmer', 'Fox', 'Chicken', 'Grain']

class State():
	global nameofpassengers
	def __init__(self, d = None):
		if d == None:
			d = {'passengers':[0,0,0,0],
			'boat':0}
		self.d = d

	def __eq__(self, s2):
		for prop in ['passengers', 'boat']:
			if self.d[prop] != s2.d[prop]:
				return False
		return True

	def __str__(self): #Produces a textual description of a state.
		p = self.d['passengers']
		txtleft = ''
		txtright = ''
		for n in range(4):
			if p[n] == LEFT:
				txtleft += nameofpassengers[n] + ' '
			else:
				txtright += nameofpassengers[n] + ' '
		txt = '\nPassenger(s) on the left side:' + txtleft + '\n'
		txt += 'passenger(s) on the right side:' + txtright + '\n'
		side = 'left'
		if self.d['boat'] == RIGHT:
			side = 'right'
		txt += "boat is on the " + side + ".\n"
		return txt

	def __hash__(self):
		return (self.__str__()).__hash__()

	def copy(self): 
		news = State({})
		news.d['passengers'] = self.d['passengers'][:]
		news.d['boat'] = self.d['boat']
		return news

	def can_move(self, targetpassenger):
		side = self.d['boat']
		passenger = self.d['passengers']
		if side != passenger[Farmer]:
			return False
		if passenger[targetpassenger] != passenger[Farmer]:
			return False
		if targetpassenger == Fox:
			if passenger[Chicken] == passenger[Grain]:
				return False
		elif targetpassenger == Grain:
			if passenger[Fox] == passenger[Chicken]:
				return False
		elif targetpassenger == Farmer:
			if passenger[Fox] == passenger[Chicken] or passenger[Chicken] == passenger[Grain]:
				return False

		return True

	def move(self, currpassenger):
		news = self.copy()
		side = self.d['boat']
		p = news.d['passengers']
		if p[int(currpassenger)] == 0:
			p[int(currpassenger)] = 1
			p[Farmer] = 1
		else :
			p[int(currpassenger)] = 0
			p[Farmer] = 0
		if side == 0:
			news.d['boat'] = 1
		else:
			news.d['boat'] = 0
		return news

def goal_test(s):
	p = s.d['passengers']
	for n in p:
		if n == 0:
			return False
	return True

def goal_message(s):
	return "Congratulations on successfully guiding all the passengers across the river!"

class Operator:
	def __init__(self, name, precond, state_transf):
		self.name = name
		self.precond = precond
		self.state_transf = state_transf

	def is_applicable(self, s):
		return self.precond(s)

	def apply(self, s):
		return self.state_transf(s)

CREATE_INITIAL_STATE = lambda: State(d={'passengers':[0,0,0,0], 'boat':0 })

OPERATORS = [Operator(
	"Cross the river with " + nameofpassengers[n],
	lambda s, n1 = int(n): s.can_move(n1),
	lambda s, n1 = int(n): s.move(n1))
	for n in range(4)
]

GOAL_TEST = lambda s: goal_test(s)

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)