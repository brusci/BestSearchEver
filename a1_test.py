#import student's function
from warehouse import *

passingMark = 15

order_list = [['Wall-E', 'Station1'], 
              ['2001: A Space Odyssey', 'Station2'], 
              ['I, Robot', 'Station3'],
              ['I, Robot', 'Station1']]
robot_list = [['Sojourner', 'idle', (12,23)], 
              ['Spirit', 'idle', (50,0)], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s1_time = 0 
s1_orders = [['2001: A Space Odyssey', 'Station2'], 
              ['I, Robot', 'Station3'],
              ['I, Robot', 'Station1']]
s1_robots = [['Sojourner', 'on_delivery', (50,0), 63], 
              ['Spirit', 'idle', (50,0)], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s2_time = 0 
s2_orders = [['Wall-E', 'Station1'], 
              ['I, Robot', 'Station3'],
              ['I, Robot', 'Station1']]
s2_robots = [['Sojourner', 'on_delivery', (20,10), 55], 
              ['Spirit', 'idle', (50,0)], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s3_time = 0 
s3_orders = [['Wall-E', 'Station1'], 
              ['2001: A Space Odyssey', 'Station2'], 
              ['I, Robot', 'Station1']]
s3_robots = [['Sojourner', 'on_delivery', (15,20), 48], 
              ['Spirit', 'idle', (50,0)], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s4_time = 0 
s4_orders = [['Wall-E', 'Station1'], 
              ['2001: A Space Odyssey', 'Station2'], 
              ['I, Robot', 'Station3']]
s4_robots = [['Sojourner', 'on_delivery', (50,0), 61], 
              ['Spirit', 'idle', (50,0)], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s5_time = 0 
s5_orders = [['2001: A Space Odyssey', 'Station2'], 
              ['I, Robot', 'Station3'],
              ['I, Robot', 'Station1']]
s5_robots = [['Sojourner', 'idle', (12,23)], 
              ['Spirit', 'on_delivery', (50,0), 94], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s6_time = 0 
s6_orders = [['Wall-E', 'Station1'], 
              ['I, Robot', 'Station3'],
              ['I, Robot', 'Station1']]
s6_robots = [['Sojourner', 'idle', (12,23)], 
              ['Spirit', 'on_delivery', (20,10), 116], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s7_time = 0 
s7_orders = [['Wall-E', 'Station1'], 
              ['2001: A Space Odyssey', 'Station2'], 
              ['I, Robot', 'Station1']]
s7_robots = [['Sojourner', 'idle', (12,23)], 
              ['Spirit', 'on_delivery', (15,20), 55], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s8_time = 0 
s8_orders = [['Wall-E', 'Station1'], 
              ['2001: A Space Odyssey', 'Station2'], 
              ['I, Robot', 'Station3']]
s8_robots = [['Sojourner', 'idle', (12,23)], 
              ['Spirit', 'on_delivery', (50,0), 68], 
              ['Curiosity', 'on_delivery', (7,0), 13]]

s9_time = 13 
s9_orders = [['Wall-E', 'Station1'], 
              ['2001: A Space Odyssey', 'Station2'], 
              ['I, Robot', 'Station3'],
              ['I, Robot', 'Station1']]
s9_robots = [['Sojourner', 'idle', (12,23)], 
              ['Spirit', 'idle', (50,0)], 
              ['Curiosity', 'idle', (7,0)]]
s_heur = 47
s1_heur = 63
s2_heur = 55
s3_heur = 48
s4_heur = 61
s5_heur = 94
s6_heur = 116
s7_heur = 55
s8_heur = 68
s9_heur = 47

totalTests = 0

if __name__ == '__main__':
    s = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                        [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                        0, 
                        [['Wall-E', 'Station1'], ['2001: A Space Odyssey', 'Station2'], ['I, Robot', 'Station3'],['I, Robot', 'Station1']], 
                        [['Sojourner', 'idle', (12,23)], ['Spirit', 'idle', (50,0)], ['Curiosity', 'on_delivery', (7,0), 13]])

    print('''Now testing your make_init_state:
                s = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                    [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                    0, 
                    [['Wall-E', 'Station1'], ['2001: A Space Odyssey', 'Station2'], ['I, Robot', 'Station3'],['I, Robot', 'Station1']], 
                    [['Sojourner', 'idle', (12,23)], ['Spirit', 'idle', (50,0)], ['Curiosity', 'on_delivery', (7,0), 13]])''')
    
    #check get_time()
    if s.get_time() == 0:
        print ("\t Time is correctly initialized, get_time() function passed this test.")
        totalTests += 1
    else:
        print ("\t ERROR: Something went wrong with your time initialization or your get_time() function:")
        print('''\t For the state generated by
                 s = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                 0, 
                [['Wall-E', 'Station1'], ['2001: A Space Odyssey', 'Station2'], ['I, Robot', 'Station3'],['I, Robot', 'Station1']], 
                [['Sojourner', 'idle', (12,23)], ['Spirit', 'idle', (50,0)], ['Curiosity', 'on_delivery', (7,0), 13]])''')
        print("\t Method s.get_time() should return 0")
        print("\t Your method returned %d"% s.get_time())   
    
    #compare get_orders() list with master list
    s_orders = s.get_orders()
    common_orders = 0
    for item in order_list:
        for student_item in s_orders:
            if (set(student_item) == set(item)):
                common_orders += 1
    
    if common_orders == 4:
        print ("\t Orders correctly initialized, get_orders() function passed this test.")
        totalTests += 1
    else:
        print ("\t ERROR: Something went wrong with your orders initialization or your get_orders() function.")
        print('''\t For the state generated by
                 s = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                 0, 
                [['Wall-E', 'Station1'], ['2001: A Space Odyssey', 'Station2'], ['I, Robot', 'Station3'],['I, Robot', 'Station1']], 
                [['Sojourner', 'idle', (12,23)], ['Spirit', 'idle', (50,0)], ['Curiosity', 'on_delivery', (7,0), 13]])''')
        print("\t Comparing s.get_orders() against the original orders param list should get exactly 4 orders in common.")
        print("\t Your method returned %d"% common_orders)  
    
    #compare get_robot_status() list with master list
    s_robots = s.get_robot_status()
    common_robots = 0
    for robot in robot_list:
        for student_robot in s_robots:
            if (set(student_robot) == set(robot)):
                common_robots += 1
            
    if common_robots == 3:
        print ("\t Robots correctly initialized, get_robot_status() function passed this test.")
        totalTests += 1
    else:
        print ("\t ERROR: Something went wrong with your robots initialization or your get_robot_status() function.")
        print('''\t For the state generated by
                 s = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                 0, 
                [['Wall-E', 'Station1'], ['2001: A Space Odyssey', 'Station2'], ['I, Robot', 'Station3'],['I, Robot', 'Station1']], 
                [['Sojourner', 'idle', (12,23)], ['Spirit', 'idle', (50,0)], ['Curiosity', 'on_delivery', (7,0), 13]])''')
        print("\t Comparing s.get_robot_status() against the original robots param list should get exactly 3 orders in common.")
        print("\t Your method returned %d"% common_robots)   
    
    print("--------------------------------")
    print("Now testing your successor state function:")
    print("\t Testing successors of initial state. Should output nine possible states:")
    
    state1 = False
    state2 = False
    state3 = False
    state4 = False
    state5 = False
    state6 = False
    state7 = False
    state8 = False
    state9 = False
    totalStates = 0
    
    #sort orders and robots from the master key
    s1_orderset = []
    for item in s1_orders:
        item = sorted(item)
        s1_orderset.append(tuple(item))
    s1_orderset.sort()

    s2_orderset = []
    for item in s2_orders:
        item = sorted(item)
        s2_orderset.append(tuple(item))
    s2_orderset.sort()
    
    s3_orderset = []
    for item in s3_orders:
        item = sorted(item)
        s3_orderset.append(tuple(item))
    s3_orderset.sort()
    
    s4_orderset = []
    for item in s4_orders:
        item = sorted(item)
        s4_orderset.append(tuple(item))
    s4_orderset.sort()
    
    s5_orderset = []
    for item in s5_orders:
        item = sorted(item)
        s5_orderset.append(tuple(item))
    s5_orderset.sort()
    
    s6_orderset = []
    for item in s6_orders:
        item = sorted(item)
        s6_orderset.append(tuple(item))
    s6_orderset.sort()
    
    s7_orderset = []
    for item in s7_orders:
        item = sorted(item)
        s7_orderset.append(tuple(item))
    s7_orderset.sort()
    
    s8_orderset = []
    for item in s8_orders:
        item = sorted(item)
        s8_orderset.append(tuple(item))
    s8_orderset.sort()
    
    s9_orderset = []
    for item in s9_orders:
        item = sorted(item)
        s9_orderset.append(tuple(item))
    s9_orderset.sort()
    
    s1_robotset = []
    for item in s1_robots:
        item = sorted([str(x) for x in item])
        s1_robotset.append(tuple(item))
    s1_robotset.sort()

    s2_robotset = []
    for item in s2_robots:
        item = sorted([str(x) for x in item])
        s2_robotset.append(tuple(item))
    s2_robotset.sort()
    
    s3_robotset = []
    for item in s3_robots:
        item = sorted([str(x) for x in item])
        s3_robotset.append(tuple(item))
    s3_robotset.sort()
    
    s4_robotset = []
    for item in s4_robots:
        item = sorted([str(x) for x in item])
        s4_robotset.append(tuple(item))
    s4_robotset.sort()
    
    s5_robotset = []
    for item in s5_robots:
        item = sorted([str(x) for x in item])
        s5_robotset.append(tuple(item))
    s5_robotset.sort()
    
    s6_robotset = []
    for item in s6_robots:
        item = sorted([str(x) for x in item])
        s6_robotset.append(tuple(item))
    s6_robotset.sort()
    
    s7_robotset = []
    for item in s7_robots:
        item = sorted([str(x) for x in item])
        s7_robotset.append(tuple(item))
    s7_robotset.sort()
    
    s8_robotset = []
    for item in s8_robots:
        item = sorted([str(x) for x in item])
        s8_robotset.append(tuple(item))
    s8_robotset.sort()
    
    s9_robotset = []
    for item in s9_robots:
        item = sorted([str(x) for x in item])
        s9_robotset.append(tuple(item))
    s9_robotset.sort()

    #test to see if all of the states are present (regardless of order)
    if(len(s.successors()) == 9):
        totalTests += 1
        for i in range (0,9):
            print(s.successors()[i].get_time())
            print(s.successors()[i].get_orders())
            print(s.successors()[i].get_robot_status())
            #sort student sets
            student_orderset = []
            for items in s.successors()[i].get_orders():
                items = sorted(items)
                student_orderset.append(tuple(items))
            student_orderset.sort() 
            
            student_robotset = []
            for itemr in s.successors()[i].get_robot_status():
                itemr = sorted([str(x) for x in itemr])
                student_robotset.append(tuple(itemr))
            student_robotset.sort() 
        
            if(s.successors()[i].get_time() == s1_time and 
                student_orderset == s1_orderset and 
                student_robotset == s1_robotset and
                state1 == False):
                    state1 = True
                    totalStates += 1
            if(s.successors()[i].get_time() == s2_time and 
                student_orderset == s2_orderset and 
                student_robotset == s2_robotset and
                state2 == False):
                    state2 = True
                    totalStates += 1
            if(s.successors()[i].get_time() == s3_time and 
                student_orderset == s3_orderset and 
                student_robotset == s3_robotset and
                state3 == False):
                    state3 = True
                    totalStates += 1
            if(s.successors()[i].get_time() == s4_time and 
                student_orderset == s4_orderset and 
                student_robotset == s4_robotset and
                state4 == False):
                    state4 = True
                    totalStates += 1
            if(s.successors()[i].get_time() == s5_time and 
                student_orderset == s5_orderset and 
                student_robotset == s5_robotset and
                state5 == False):
                    state5 = True
                    totalStates += 1
            if(s.successors()[i].get_time() == s6_time and 
                student_orderset == s6_orderset and 
                student_robotset == s6_robotset and
                state6 == False):
                    state6 = True
                    totalStates += 1
            if(s.successors()[i].get_time() == s7_time and 
                student_orderset == s7_orderset and 
                student_robotset == s7_robotset and
                state7 == False):
                    state7 = True
                    totalStates += 1
            if(s.successors()[i].get_time() == s8_time and 
                student_orderset == s8_orderset and 
                student_robotset == s8_robotset and
                state8 == False):
                    state8 = True
                    totalStates += 1
            if(s.successors()[i].get_time() == s9_time and 
                student_orderset == s9_orderset and 
                student_robotset == s9_robotset and
                state9 == False):
                    state9 = True
                    totalStates += 1
            
        if(totalStates == 9):
            print ("\t 9 out of 9 states were correct for the successor function.")
            totalTests += 1
        else:
            print ("\t ERROR: Only %d out of 9 states were correct. Something's wrong with your successor function:" % totalStates)
            if (state1 == False):
                print("\t Missing state:")
                print("\t", s1_time)
                print("\t", s1_orders)
                print("\t", s1_robots)
            if (state2 == False):
                print("\t Missing state:")
                print("\t", s2_time)
                print("\t", s2_orders)
                print("\t", s2_robots)
            if (state3 == False):
                print("\t Missing state:")
                print("\t", s3_time)
                print("\t", s3_orders)
                print("\t", s3_robots)
            if (state4 == False):
                print("\t Missing state:")
                print("\t", s4_time)
                print("\t", s4_orders)
                print("\t", s4_robots)
            if (state5 == False):
                print("\t Missing state:")
                print("\t", s5_time)
                print("\t", s5_orders)
                print("\t", s5_robots)
            if (state6 == False):
                print("\t Missing state:")
                print("\t", s6_time)
                print("\t", s6_orders)
                print("\t", s6_robots)
            if (state7 == False):
                print("\t Missing state:")
                print("\t", s7_time)
                print("\t", s7_orders)
                print("\t", s7_robots)
            if (state8 == False):
                print("\t Missing state:")
                print("\t", s8_time)
                print("\t", s8_orders)
                print("\t", s8_robots)
            if (state9 == False):
                print("\t Missing state:")
                print("\t", s9_time)
                print("\t", s9_orders)
                print("\t", s9_robots)
    else:
        print("\t ERROR: You have an incorrect number of states in your successor function.")
        print("\t We expect to have 9 states in s.successors().")
        print("\t Your function only returned %d" % totalStates)
   
    print("--------------------------------")
    print("Now testing your heuristic:")
    if(heur_min_completion_time(s) == s_heur):
        totalTests += 1
        print("\t Initial state heuristic time is correct.")
    else:
        print("\t Initial state heuristic wrong. Something's wrong with your heuristic.")
        print("\t heur_min_completion_time(s) should return %d" % s_heur)
        print("\t Your function returned %d" % heur_min_completion_time(s))
    
    heur1 = False
    heur2 = False
    heur3 = False
    heur4 = False
    heur5 = False
    heur6 = False
    heur7 = False
    heur8 = False
    heur9 = False
    totalHeurs = 0
    
    if(len(s.successors()) == 9):
        for i in range (0,9):
            if(heur_min_completion_time(s.successors()[i]) == s1_heur and heur1 == False):
                heur1 = True
                totalHeurs += 1
            if(heur_min_completion_time(s.successors()[i]) == s2_heur and heur2 == False):
                heur2 = True
                totalHeurs += 1
            if(heur_min_completion_time(s.successors()[i]) == s3_heur and heur3 == False):
                heur3 = True
                totalHeurs += 1
            if(heur_min_completion_time(s.successors()[i]) == s4_heur and heur4 == False):
                heur4 = True
                totalHeurs += 1
            if(heur_min_completion_time(s.successors()[i]) == s5_heur and heur5 == False):
                heur5 = True
                totalHeurs += 1
            if(heur_min_completion_time(s.successors()[i]) == s6_heur and heur6 == False):
                heur6 = True
                totalHeurs += 1
            if(heur_min_completion_time(s.successors()[i]) == s7_heur and heur7 == False):
                heur7 = True
                totalHeurs += 1
            if(heur_min_completion_time(s.successors()[i]) == s8_heur and heur8 == False):
                heur8 = True
                totalHeurs += 1
            if(heur_min_completion_time(s.successors()[i]) == s9_heur and heur9 == False):
                heur9 = True
                totalHeurs += 1
    
        if(totalHeurs == 9):
            print ("\t 9 out of 9 tested heuristics were correct.")
            totalTests += 1
        else:
            print ("\t ERROR: Only %d out of 9 tested heuristics were correct." % totalHeurs)  
            print ('''\t Calling heur_min_completion_time() on s.successors() should return heuristics for nine states: 
                    %d, %d, %d, %d, %d, %d, %d, %d, and %d.''' % (s1_heur, s2_heur, s3_heur, s4_heur, s5_heur, s6_heur, s7_heur, s8_heur, s9_heur))  
            if(heur1 == False):
                print("\t You are missing %d" % s1_heur)
            if(heur2 == False):
                print("\t You are missing %d" % s2_heur)
            if(heur3 == False):
                print("\t You are missing %d" % s3_heur)
            if(heur4 == False):
                print("\t You are missing %d" % s4_heur)
            if(heur5 == False):
                print("\t You are missing %d" % s5_heur)
            if(heur6 == False):
                print("\t You are missing %d" % s6_heur)
            if(heur7 == False):
                print("\t You are missing %d" % s7_heur)
            if(heur8 == False):
                print("\t You are missing %d" % s8_heur)
            if(heur9 == False):
                print("\t You are missing %d" % s9_heur)
    print("--------------------------------")
    print("Now testing time updates (set 1 of 2 tests):")
    s2 = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                        [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                        0, 
                        [['Wall-E', 'Station3']], 
                        [['Sojourner', 'on_delivery', (20,10), 11], ['Spirit', 'on_delivery', (50,0), 11]])
    print('''\t Initializing state where two robots are scheduled to complete at the same time. Only successor should idle both robots:
                s2 = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                        [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                        0, 
                        [['Wall-E', 'Station3']], 
                        [['Sojourner', 'on_delivery', (20,10), 11], ['Spirit', 'on_delivery', (50,0), 11]]) ''')
    if(len(s2.successors()) == 1):
        totalTests += 1
        if (s2.successors()[0].get_time() == 11):
            totalTests += 1
            print("\t Time correctly advanced to 11.")
        else:
            print("\t ERROR: Time not correctly advanced in the successor state.")
            print("\t The successor state should advance time to 11.")
            print("\t Your successor state advances time to %d." % s2.successors()[0].get_time())
        
        if(len(s2.successors()[0].get_robot_status()) == 2):
            totalTests += 1
            
            student_robotset2 = []
            for itemr in s2.successors()[0].get_robot_status():
                itemr = sorted([str(x) for x in itemr])
                student_robotset2.append(tuple(itemr))
            student_robotset2.sort() 
            sr1 = student_robotset2[0]
            sr2 = student_robotset2[1]
            
            unsorted_robot_list_2 = [['Sojourner', 'idle', (20,10)], ['Spirit', 'idle', (50,0)]]
            robot_list_2 = []
            for itemr in unsorted_robot_list_2:
                itemr = sorted([str(x) for x in itemr])
                robot_list_2.append(tuple(itemr))
            robot_list_2.sort()
            r1 = robot_list_2[0]
            r2 = robot_list_2[1]
            
            robot1 = False
            robot2 = False
            totalRobots = 0
            
            if(sr1 == r1 and robot1 == False):
                robot1 = True
                totalRobots += 1   
            if(sr2 == r1 and robot1 == False):
                robot1 = True
                totalRobots += 1                            
            if(sr1 == r2 and robot2 == False):
                robot2 = True
                totalRobots += 1    
            if(sr2 == r2 and robot2 == False):
                robot2 = True
                totalRobots += 1                                      
            
            if (totalRobots == 2):
                print("\t Both robots in successor state successfully idled.")
                totalTests += 1
            else:
                print("\t ERROR: One or more of your robots has an incorrect status.")
                print("\t We were expecting: [['Sojourner', 'idle', (20,10)], ['Spirit', 'idle', (50,0)]]")
                print("\t Your function returned: ", s2.successors()[0].get_robot_status())
        else:
            print("\t ERROR: Successor function returned the wrong number of robots.")
            print('''\t s2.successors()[0].get_robot_status()) should return two robots''')
            print("\t Your successor function returned %d robot(s)." % len(s2.successors()[0].get_robot_status()))   
    else:
        print("\t ERROR: Something's wrong with your successor function.")
        print('''\t s2.successors() should only have 1 successor with time = 11 and robot status:
                [['Sojourner', 'idle', (20,10)], ['Spirit', 'idle', (50,0)]]''')
        print("\t Your successor function returned %d state(s)." % len(s2.successors()))
    
    print("--------------------------------")
    
    print("Now testing time updates (set 2 of 2 tests):")
    s3 = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                        [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                        0, 
                        [['Wall-E', 'Station3']], 
                        [['Sojourner', 'on_delivery', (20,10), 7], ['Spirit', 'on_delivery', (50,0), 23]])
    print('''\t Initializing state where two robots are scheduled to complete at different times:
                s3 = make_init_state([['I, Robot', (19,3)], ['2001: A Space Odyssey', (3,31)], ['Wall-E', (11, 8)]], 
                        [['Station1', (50,0)], ['Station2', (20,10)], ['Station3', (15,20)]],
                        0, 
                        [['Wall-E', 'Station3']], 
                        [['Sojourner', 'on_delivery', (20,10), 7], ['Spirit', 'on_delivery', (50,0), 23]]) 
                Time step should move to that of the soonest delivery.''')
    
    if(len(s3.successors()) == 1):
        totalTests += 1
        if (s3.successors()[0].get_time() == 7):
            totalTests += 1
            print("\t Time correctly advanced to 7.")
        else:
            print("\t ERROR: Time not correctly advanced in the successor state.")
            print("\t The successor state should advance time to 7.")
            print("\t Your successor state advances time to %d." % s3.successors()[0].get_time())
        
        if(len(s3.successors()[0].get_robot_status()) == 2):
            totalTests += 1
            
            student_robotset3 = []
            for itemr in s3.successors()[0].get_robot_status():
                itemr = sorted([str(x) for x in itemr])
                student_robotset3.append(tuple(itemr))
            student_robotset3.sort() 
            sr_3_1 = student_robotset3[0]
            sr_3_2 = student_robotset3[1]
            
            unsorted_robot_list_3 = [['Sojourner', 'idle', (20,10)], ['Spirit', 'on_delivery', (50,0), 23]]
            robot_list_3 = []
            for itemr in unsorted_robot_list_3:
                itemr = sorted([str(x) for x in itemr])
                robot_list_3.append(tuple(itemr))
            robot_list_3.sort()
            r_3_1 = robot_list_3[0]
            r_3_2 = robot_list_3[1]
            
            robot_3_1 = False
            robot_3_2 = False
            totalRobots_3 = 0
            
            if(sr_3_1 == r_3_1 and robot_3_1 == False):
                robot_3_1 = True
                totalRobots_3 += 1  
            if(sr_3_2 == r_3_1 and robot_3_1 == False):
                robot_3_1 = True
                totalRobots_3 += 1                           
            if(sr_3_1 == r_3_2 and robot_3_2 == False):
                robot_3_2 = True
                totalRobots_3 += 1    
            if(sr_3_2 == r_3_2 and robot_3_2 == False):
                robot_3_2 = True
                totalRobots_3 += 1                                       
            
            if (totalRobots_3 == 2):
                print("\t Both robots in successor state successfully updated.")
                totalTests += 1
            else:
                print("\t ERROR: One or more of your robots has an incorrect status.")
                print("\t We were expecting: [['Sojourner', 'idle', (20,10)], ['Spirit', 'on_delivery', (50,0), 23]]")
                print("\t Your function returned: ", s3.successors()[0].get_robot_status())
        else:
            print("\t ERROR: Successor function returned the wrong number of robots.")
            print('''\t s3.successors()[0].get_robot_status()) should return two robots''')
            print("\t Your successor function returned %d robot(s)." % len(s3.successors()[0].get_robot_status()))   
    else:
        print("\t ERROR: Something's wrong with your successor function.")
        print('''\t s3.successors() should only have 1 successor with time = 7 and robot status:
                [['Sojourner', 'idle', (20,10)], ['Spirit', 'on_delivery', (50,0), 23]]''')
        print("\t Your successor function returned %d state(s)." % len(s3.successors()))
    
    print("--------------------------------")
    if(totalTests == passingMark):
        print("All tests passed. Good job!")
    else:
        print("Some errors were found. Go back and check the output.")