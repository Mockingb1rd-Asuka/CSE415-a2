'''Farmer_Fox.py
by Jerry Hong
UWNetID: yh47
Student number: 1663445

Assignment 2, in CSE 415, Winter 2020.
 
This file contains my problem formulation for the problem of
the Farmer, Fox, Chicken, and Grain.
'''

# Put your formulation of the Farmer-Fox-Chicken-and-Grain problem here.
# Be sure your name, uwnetid, and 7-digit student number are given above in 
# the format shown.

# </METADATA>
SOLUZION_VERSION = "2.0"
PROBLEM_NAME = "Farmer Fox"
PROBLEM_VERSION = "2.0"
PROBLEM_AUTHORS = ['Jerry Hong']
PROBLEM_CREATION_DATE = "22-JAN-2020"

PROBLEM_DESC = \
    '''
'''

# </METADATA>

# <COMMON_DATA>
# </COMMON_DATA>

# <COMMON_CODE>
Fox = 0
Chicken = 1
Grain = 2
Farmer = 3
LEFT = 0
RIGHT = 1
passenger_name = ["fox", "chicken", "grain"]
passenger_with_farmer = ["fox", "chicken", "grain", "farmer"]  # farmer is always with the boat


class State():

    def __init__(self, d=None):
        if d == None:
            d = {'passenger': [LEFT, LEFT, LEFT],
                 'boat': LEFT}
        self.d = d

    def __eq__(self, s2):
        for p in ['passenger', 'boat']:
            if self.d[p] != s2.d[p]: return False
        return True

    def __str__(self):
        # Produces a textual description of a state.
        # Might not be needed in normal operation with GUIs.
        p = self.d['passenger']
        if self.d['boat'] == LEFT:
            side = "left"
        else:
            side = "right"
        on_the_left = ""
        on_the_right = ""
        for index, passenger in enumerate(passenger_name):
            if p[index] == LEFT:
                on_the_left += passenger_name[index] + " "
            else:
                on_the_right += passenger_name[index] + " "
        txt = "\n On the left: " + on_the_left
        txt += "\n On the right: " + on_the_right
        txt += "\n farmer and boat are on the " + side + ".\n"
        return txt

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State({})
        news.d['passenger'] = self.d['passenger'][:]
        news.d['boat'] = self.d['boat']
        return news

    def can_move(self, passenger):
        '''Tests whether it's legal to move the boat and take
         fox and chicken and grain.'''
        p = self.d['passenger']
        if passenger == Farmer:  # no change in place of fox, chicken and grain
            return p[Fox] != p[Chicken] and p[Chicken] != p[Grain]
        elif p[passenger] != self.d['boat']: # cannot move without farmer
            return False
        elif passenger == Fox:  # no change in place of chicken and grain
            return p[Chicken] != p[Grain]
        elif passenger == Grain:  # no change in place of fox and chicken
            return p[Fox] != p[Chicken]
        else:  # moving chicken is always safe
            return True

    def move(self, passenger):
        news = self.copy()
        p = self.d['passenger']
        b = self.d['boat']
        if passenger != Farmer:
            news.d['passenger'][passenger] = 1 - p[passenger]
        news.d['boat'] = 1 - b
        return news


def goal_test(s):
    '''If fox chicken and grain are on the right, then s is a goal state.'''
    p = s.d['passenger']
    return p[Fox] == RIGHT and p[Chicken] == RIGHT and p[Grain] == RIGHT


def goal_message(s):
    return "Congratulations on successfully guiding the fox chicken and grain across the river!"


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)


# </COMMON_CODE>

# <INITIAL_STATE>
CREATE_INITIAL_STATE = lambda: State(d={'passenger': [LEFT, LEFT, LEFT], 'boat': LEFT})
# </INITIAL_STATE>

# <OPERATORS>

OPERATORS = [
    Operator(
        "Cross the river with " + passenger_with_farmer[index],
        lambda s, p1=index: s.can_move(p1),
        lambda s, p1=index: s.move(p1))
    for (index, name) in enumerate(passenger_with_farmer)]
# </OPERATORS>


# <GOAL_TEST> (optional)
GOAL_TEST = lambda s: goal_test(s)
# </GOAL_TEST>

# <GOAL_MESSAGE_FUNCTION> (optional)
GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
# </GOAL_MESSAGE_FUNCTION>
