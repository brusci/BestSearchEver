#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented to complete the warehouse domain.  

'''
warehouse STATESPACE 
'''
#   You may add only standard python imports---i.e., ones that are automatically
#   available on CDF.
#   You may not remove any imports.
#   You may not import or otherwise source any of your own files

from search import *
from random import randint
import copy

##################################################
# The search space class 'game'                  #
# This class is a sub-class of 'StateSpace'      #
##################################################

class game(StateSpace):
    def __init__(self, action, gval, size, current_time, obstacles_list, player, enemy, parent = None):
        StateSpace.__init__(self, action, gval, parent)
        self.size = size #symmetrical size of game board
        self.current_time = current_time
        self.obstacles_list = obstacles_list #list of unnavigable loc
        self.player = player
        self.enemy = enemy
        #Each player and enemy itself a list in the format [x, y]
        
#IMPLEMENT
        """Initialize a game search state object."""

    def get_obstacles_list(self):
        #return list of obstacles
        return obstacles_list
            
    def find_min_delivery(self):
        tmp = [] #return min delivery action time
        for robot in self.robot_status:
            if (len(robot) > 3):
                tmp.append(robot[3])
        if (not tmp):
            return 0
        return min(tmp)   

    def successors(self):
    #IMPLEMENT    
        States = list()

        iterate_copy = copy.deepcopy(self.get_orders())
        for order in iterate_copy:
            for robot in self.robot_status:
                orders_copy = copy.deepcopy(iterate_copy)
                robots_copy = copy.deepcopy(self.get_robot_status())
                if (robot[1] == 'idle'):
                    product_coords = self.find_product_loc(order[0])
                    station_coords = self.find_station_loc(order[1])
                    robot_to_product = abs(robot[2][0] - product_coords[0]) + abs(robot[2][1] - product_coords[1])
                    product_to_station = abs(product_coords[0] - station_coords[0]) + abs(product_coords[1] - station_coords[1])
                    
                    robot_copy = copy.deepcopy(robot) #make a copy of robot and change it's coords, status, and action time
                    robot_copy[1] = 'on_delivery'
                    robot_copy[2] = station_coords
                    robot_copy.append(robot_to_product + product_to_station)
                    robots_copy[robots_copy.index(robot)] = robot_copy
                    orders_copy.remove(order)
                    
                    action_print = "deliver({},{},{}).".format(robot_copy[0],order[0],order[1])
                    States.append( warehouse(action_print, self.gval+1, self.product_list, self.packing_station_list, self.current_time, orders_copy, robots_copy, self) )
                    
        robots_copy2 = copy.deepcopy(self.get_robot_status())
        orders_copy2 = copy.deepcopy(self.get_orders())  
        min_move = self.find_min_delivery() #take the minimum of all action-cost on-delivery robots
        action_print = "move_forward({})".format(min_move)
        new_time = self.current_time + min_move
        deliver_add = 0

        for robot in robots_copy2:
            deliver_add +=1
            if ((robot[1] == 'on_delivery') and (robot[3] <= min_move)): #if on-delivery and time cost is less than min_move, update
                robot[1] = 'idle'
                del robot[-1]
        if (deliver_add > 0): #check if at least one action has been made, if so this is a new state and must be appended
            States.append( warehouse(action_print, self.gval+1, self.product_list, self.packing_station_list, new_time, orders_copy2, robots_copy2, self) )
        return States
        '''Return list of warehouse objects that are the successors of the current object'''
    

    def hashable_state(self):
#IMPLEMENT
        return (str(self.current_time) + str(self.robot_status) + str(self.open_orders))
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent the state.'''
        
    def print_state(self):
        #DO NOT CHANGE THIS FUNCTION---it will be used in auto marking
        #and in generating sample trace output. 
        #Note that if you implement the "get" routines below properly, 
        #This function should work irrespective of how you represent
        #your state. 

        if self.parent:
            print("Action= \"{}\", S{}, g-value = {}, (From S{})".format(self.action, self.index, self.gval, self.parent.index))
        else:
            print("Action= \"{}\", S{}, g-value = {}, (Initial State)".format(self.action, self.index, self.gval))
            
        print("Time = {}".format(self.get_time()))
        print("Unfulfilled Orders")
        for o in self.get_orders():
            print("    {} ==> {}".format(o[0], o[1]))
        print("Robot Status")
        for rs in self.get_robot_status():
            print("    {} is {}".format(rs[0], rs[1]), end="")
            if rs[1] == 'idle':
                print(" at location {}".format(rs[2]))
            elif rs[1] == 'on_delivery':
                print(" will be at location {} at time {}".format(rs[2], rs[3]))

#Data accessor routines.

    def get_robot_status(self):
#IMPLEMENT

        '''robot_list = []
        
        for robot in self.robot_status:
            tmp = []
            tmp.append(robot[0])
            tmp.append(robot[1])
            tmp.append(robot[2])                #ex ('r2', 'idle', (0,0))
            if (robot[1] == "on_delivery"): #ex ('r1', 'on_delivery', (20,10), 14)
                tmp.append(robot[3])
            robot_list.append(tmp)
            '''
        return self.robot_status
            
        
        '''Return list containing status of each robot
           This list has to be in the format: [rs_1, rs_2, ..., rs_k]
           with one status list for each robot in the state. 
           Each robot status item rs_i is itself a list in the format [<name>, <status>, <loc>, <ftime>]
           Where <name> is the name of the robot (a string)
                 <status> is either the string "idle" or the string "on_delivery"
                 <loc> is a location (a pair (x,y)) 
                       if <status> == "idle" then loc is the robot's current location
                       if <status> == "on_delivery" then loc is the robot's future location
                <ftime> 
                       if <status> == "idle" this item is missing (i.e., the list is of 
                                      length 3)
                       if <status> == "on_delivery" then this is a number that is the 
                                      time that the robot will complete its current delivery
        '''

    def get_time(self):
#IMPLEMENT
        return self.current_time
        '''Return the current time of this state (a number)'''

    def get_orders(self):
        
#IMPLEMENT
        return self.open_orders
        '''Return list of unfulfilled orders of this state
           This list is in the format [o1, o2, ..., om]
           one item for each unfulfilled order. 
           Each oi is itself a list [<product_name>, <packing_station_name>]
           where <product_name> is the name of the product to be delivered
           and  <packing_station_name> is the name of the packing station it is to be delivered to'''

#############################################
# heuristics                                #
#############################################
    
def heur_zero(state):
    '''Zero Heuristic use to make A* search perform uniform cost search'''
    return 0

def heur_min_completion_time(state):
#IMPLEMENT
    '''warehouse heuristic'''
    #We want an admissible heuristic. Since the aim is to delivery all
    #of the products to their packing station in as short as a time as
    #possible. 
    #NOTE that we want an estimate of the ADDED time beyond the current
    #     state time.
    #Consider all of the possible delays in moving from this state to
    #a final delivery of all orders.
    # 1. All robots have to finish any current delivery they are on.
    #    So the earliest we could finish is the 
    #    maximum over all robots on delivery of 
    #       (robot's finish time - the current state time)
    #    we subtract the current state time because we want time
    #    beyond the current time required to complete the delivery
    #    Let this maximum be TIME1.
    #    Clearly we cannot finish before TIME1
    #
    # 2. For all unfulfilled orders we need to pick up the product of
    #    that order with some robot, and then move it to the right
    #    packing station. However, we could do many of these
    #    deliveries in parallel. So to get an *admissible* heuristic
    #    we take the MAXIMUM of a MINUMUM time any unfulfilled order
    #    can be completed. There are many different minimum times that
    #    could be computed...of varying complexity. For simplicity we
    #    ignore the time required to get a robot to package, and
    #    instead take the time to move the package from its location
    #    to the packing station location as being a suitable minimum.
    #    So we compute these minimums, then take the maximum of these
    #    minimums Call this max TIME2
    #    Clearly we cannot finish before TIME2
    #
    # Finally we return as a the heuristic value the MAXIMUM of ITEM1 and ITEM2
    
    delivery_times = []
    TIME1 = 0
    TIME2 = 0
    for robot in state.robot_status:
        if (len(robot) > 3):
            delivery_times.append(robot[3])
    if (delivery_times != []):
        TIME1 = (max(delivery_times) - state.current_time)
        
    station_distances = []
    for product in state.product_list:
        for station in state.packing_station_list:
            if ([product[0], station[0]] in state.open_orders):
                station_distances.append(abs(product[1][0] - station[1][0]) + abs(product[1][1] - station[1][1]))
                #print("product to station distances: ", abs(product[1][0] - station[1][0]) + abs(product[1][1] - station[1][1]))
    if (station_distances != []):
        TIME2 = max(station_distances) 
    return max(TIME1, TIME2)

def game_goal_fn(state):
#IMPLEMENT
    '''Have we reached the goal when an enemy is on same loc as player'''
    if (state.player[1 == state.enemy.loc):
        return True
    return False

def make_init_state(size, current_time, obstacles_list, player, enemy):
#IMPLEMENT

    return game("START", 0, size, current_time, obstacles_list, player, enemy)
    
    
    '''Input the following items which specify a state and return a warehouse object 
       representing this initial state.
         The state's its g-value is zero
         The state's parent is None
         The state's action is the dummy action "START"
         
       product_list = [p1, p2, ..., pk]
          a list of products. Each product pi is itself a list
          pi = [product_name, (x,y)] where 
              product_name is the name of the product (a string) and (x,y) is the
              location of that product.
              
       packing_station = [ps1, ps2, ..., psn]
          a list of packing stations. Each packing station ps is itself a list
          pi = [packing_station_name, (x,y)] where 
              packing_station_name is the name of the packing station (a string) and (x,y) is the
              location of that station.
       current_time = an integer >= 0
          The state's current time.
          
       open_orders = [o1, o2, ..., om] 
          a list of unfulfilled (open) orders. Each order is itself a list
          oi = [product_name, packing_station_name] where
               product_name is the name of the product (a string) and
               packing_station_name is the name of the packing station (a string)
               The order is to move the product to the packing station
               
        robot_status = [rs1, rs2, ..., rsk]
          a list of robot and their status. Each item is itself a list  
          rsi = ['name', 'idle'|'on_delivery', (x, y), <finish_time>]   
            rsi[0] robot name---a string 
            rsi[1] robot status, either the string "idle" or the string
                  "on_delivery"
            rsi[2] robot's location--if "idle" this is the current robot's
                   location, if "on_delivery" this is the robots final future location
                   after it has completed the delivery
            rsi[3] the finish time of the delivery if the "on_delivery" 
                   this element of the list is absent if robot is "idle" 

   NOTE: for simplicity you may assume that 
         (a) no name (robot, product, or packing station is repeated)
         (b) all orders contain known products and packing stations
         (c) all locations are integers (x,y) where both x and y are >= 0
         (d) the robot status items are correctly formatted
         (e) the future time for any robot on_delivery is >= to the current time
         (f) the current time is >= 0
    '''

########################################################
#   Functions provided so that you can more easily     #
#   Test your implementation                           #
########################################################

def make_rand_init_state(nprods, npacks, norders, nrobots):
    '''Generate a random initial state containing 
       nprods = number of products
       npacks = number of packing stations
       norders = number of unfulfilled orders
       nrobots = number of robots in domain'''
    prods = []
    for i in range(nprods):
        ii = int(i)
        prods.append(["product{}".format(ii), (randint(0,50), randint(0,50))])
    packs = []
    for i in range(npacks):
        ii = int(i)
        packs.append(["packing{}".format(ii), (randint(0,50), randint(0,50))])
    orders = []
    for i in range(norders):
        orders.append([prods[randint(0,nprods-1)][0], packs[randint(0,npacks-1)][0]])
    robotStatus = []
    for i in range(nrobots):
        ii = int(i)
        robotStatus.append(["robot{}".format(ii), "idle", (randint(0,50), randint(0,50))])
    return make_init_state(prods, packs, 0, orders, robotStatus)


def test(nprods, npacks, norders, nrobots):
    s0 = make_rand_init_state(nprods, npacks, norders, nrobots)
    se = SearchEngine('astar', 'full')
    se.trace_on(2)
    final = se.search(s0, warehouse_goal_fn, heur_min_completion_time)
