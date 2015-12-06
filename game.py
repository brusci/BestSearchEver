'''
game STATESPACE 
'''

from search import *
from random import randint
import copy

##################################################
# The search space class 'game'                  #
# This class is a sub-class of 'StateSpace'      #
##################################################

class game(StateSpace):
    def __init__(self, action, gval, size, current_time, obstacles_list, player, enemy, parent = None):
        """Initialize a game search state object."""
        # IMPLEMENT
        StateSpace.__init__(self, action, gval, parent)
        self.size = size # symmetrical size of game board
        self.current_time = current_time
        self.obstacles_list = obstacles_list #list of unnavigable loc
        self.player = copy.deepcopy(player)
        self.enemy = enemy
                                
        # Each player and enemy itself a list in the format [x, y]
        
    def get_obstacles_list(self):
        # return list of obstacles
        return obstacles_list
            
    def find_min_delivery(self):
        tmp = [] # return min delivery action time
        for robot in self.robot_status:
            if (len(robot) > 3):
                tmp.append(robot[3])
        if (not tmp):
            return 0
        return min(tmp)   

    def successors(self):
        #IMPLEMENT    
        States = list()
        
        # Try moving enemy LEFT
        if (self.enemy[0] - 1 >= 0):
            enemy_copy = copy.deepcopy(self.enemy) # make a copy of the enemy and
                                                   # change its coords
            enemy_copy[0] = self.enemy[0] - 1
            enemy_copy[1] = self.enemy[1]
            new_enemy_to_player = abs(enemy_copy[0] - self.player[0]) + abs(enemy_copy[1] - self.player[1])
            enemy_copy.append(new_enemy_to_player)
            old_enemy_to_player = abs(self.enemy[0] - self.player[0]) + abs(self.enemy[1] - self.player[1])
            
            action_print = "move_to({},{})".format(enemy_copy[0], enemy_copy[1])
            States.append( game(action_print, self.gval+1, self.size, self.current_time+1, self.obstacles_list, self.player, enemy_copy, self) )
        
        # Try moving enemy RIGHT
        if (self.enemy[0] - 1 < self.size):
            enemy_copy = copy.deepcopy(self.enemy) # make a copy of the enemy and
                                                   # change its coords
            enemy_copy[0] = self.enemy[0] + 1
            enemy_copy[1] = self.enemy[1]
            new_enemy_to_player = abs(enemy_copy[0] - self.player[0]) + abs(enemy_copy[1] - self.player[1])
            enemy_copy.append(new_enemy_to_player)
            old_enemy_to_player = abs(self.enemy[0] - self.player[0]) + abs(self.enemy[1] - self.player[1])
            
            action_print = "move_to({},{})".format(enemy_copy[0], enemy_copy[1])
            States.append( game(action_print, self.gval+1, self.size, self.current_time+1, self.obstacles_list, self.player, enemy_copy, self) )
        
        # Try moving enemy UP
        if (self.enemy[1] - 1 >= 0):
            enemy_copy = copy.deepcopy(self.enemy) # make a copy of the enemy and
                                                   # change its coords
            enemy_copy[0] = self.enemy[0]
            enemy_copy[1] = self.enemy[1] - 1
            new_enemy_to_player = abs(enemy_copy[0] - self.player[0]) + abs(enemy_copy[1] - self.player[1])
            enemy_copy.append(new_enemy_to_player)
            old_enemy_to_player = abs(self.enemy[0] - self.player[0]) + abs(self.enemy[1] - self.player[1])
            
            action_print = "move_to({},{})".format(enemy_copy[0],enemy_copy[1])
            States.append( game(action_print, self.gval+1, self.size, self.current_time+1, self.obstacles_list, self.player, enemy_copy, self) )
        
        # Try moving enemy DOWN
        if (self.enemy[1] - 1 < self.size):
            enemy_copy = copy.deepcopy(self.enemy) # make a copy of the enemy and
                                                   # change its coords
            enemy_copy[0] = self.enemy[0]
            enemy_copy[1] = self.enemy[1] + 1
            new_enemy_to_player = abs(enemy_copy[0] - self.player[0]) + abs(enemy_copy[1] - self.player[1])
            enemy_copy.append(new_enemy_to_player)
            old_enemy_to_player = abs(self.enemy[0] - self.player[0]) + abs(self.enemy[1] - self.player[1])
            
            action_print = "move_to({},{})".format(enemy_copy[0],enemy_copy[1])
            States.append( game(action_print, self.gval+1, self.size, self.current_time+1, self.obstacles_list, self.player, enemy_copy, self) )
        
        return States
    
    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''
    # IMPLEMENT
#         return (str(self.player) + str(self.enemy) + str(self.current_time))
        return (copy.deepcopy(self.enemy[0]), copy.deepcopy(self.enemy[1]))
        
    def print_state(self):
        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))
            
        print("Time = {}".format(self.get_time()))
        print("Enemy is at location({},{})".format(self.enemy[0], self.enemy[1]))
        print("Player is at location({},{})".format(self.player[0], self.player[1]))
        print()

    # Data accessor routines.
    def get_time(self):
    # IMPLEMENT
        '''Return the current time of this state (a number)'''
        return self.current_time
        

#############################################
# heuristics                                #
#############################################
    
def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0

def heur_min_completion_time(state):
#IMPLEMENT
    '''game heuristic'''
    # We want an admissible heuristic. Since the aim is to reach the 
    # player in as short as a time as possible. We cannot finish until
    # a distance between the enemy and the player has been reached. So the
    # earliest we could finish is:
    #   abs(enemy_x - player_x) + abs(enemy_y - player_y)
    # We return this value as a heuristic
    
    return abs(state.enemy[0] - state.player[0]) + abs(state.enemy[1] - state.player[1])

def game_goal_fn(state):
    '''Have we reached the goal when an enemy is on same loc as player'''
    # IMPLEMENT
    if (state.player[0] == state.enemy[0] and state.player[1] == state.enemy[1]):
        return True
    return False

def make_init_state(size, current_time, obstacles_list, player, enemy):
    '''Input the following items which specify a state and return a warehouse object 
       representing this initial state.
         The state's its g-value is zero
         The state's parent is None
         The state's action is the dummy action "START"
         
         current_time = an integer >= 0
          The state's current time.
          
         obstacles_list = [o1, o2, ..., ok]
          a list of coordinates of obstacles. Each obstacle oi is itself an obstacle
          oi = [x,y] where 
            x is the x coordinate of the obstacle, and y is the y coordinate.
            
         player = [x, y]
          The player's location, where 
            x is the x-coordinate of the obstacle, and y is the y-coordinate.
        
         enemy = [x, y]
          The enemy's location, where 
            x is the x-coordinate of the obstacle, and y is the y-coordinate.
          '''
    # IMPLEMENT

    return game("START", 0, size, current_time, obstacles_list, player, enemy, [])

########################################################
#   Functions provided so that you can more easily     #
#   Test your implementation                           #
########################################################

def make_rand_init_state(nsize, nobstacles):
    '''Generate a random initial state containing 
       nsize = size of the board - one length
       nobstacles = number of obstacles'''
    size = randint(0,50)
    
    obstacles_list = []
    for i in range(nobstacles):
        ii = int(i)
        obstacles_list.append([(randint(0,size), randint(0,size))])
        
    player = [randint(0,size),randint(0,size)]
    enemy = [randint(0,size),randint(0,size)]
    while (enemy[0] == player[0] and enemy[1] == player[1]):
        enemy = [randint(0,size),randint(0,size)]
    return make_init_state(size, 0, obstacles_list, player, enemy)


def test(nsize, nobstacles):
    s0 = make_rand_init_state(nsize, nobstacles)
    se = SearchEngine('astar', 'full')
    se.trace_on(2)
    final = se.search(s0, game_goal_fn, heur_min_completion_time)