from game import *

def test(se, s, strategy, cycle, goal_fn, heur=None):
    se.set_strategy(strategy, cycle)
        
    strat_name = 'Depth first'
    
    if strategy == 'breadth_first':
        strat_name = 'Breadth first'
    elif strategy == 'astar':
        strat_name = 'Astar'
    
    cycle_name = 'with heur_min_completion_time heuristic'
    
    if cycle == 'full':
        cycle_name = '(full cycle checking)'
    elif cycle == 'path':
        cycle_name = 'with only path checking'
    elif cycle == 'none':
        cycle_name = 'with no cycle checking'
    
    print("========={} {}=====".format(strat_name, cycle_name))
    if strategy == 'astar':
        se.search(s, goal_fn, heur)   
    else:
        se.search(s, goal_fn)
    print("===================================================")
    print("")

if __name__ == '__main__':

    # ====adjust these values to change test parameters:=====
    size = 10
    obstacles_list = []
    player = [1, 1]
    enemy = [0, 0]

    se = SearchEngine('astar', 'full')

    # ===== If you want to trace the search (use trace level 1 for illustration):
#     se.trace_on(2)
#     se.trace_on(1)
    
    # ======Uncomment pairs of lines to test each of:======
    # DFS, BFS, and A*, each with cycle checking options of: none, path, and full
    # =====================================================
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'depth_first', 'none', game_goal_fn)
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'depth_first', 'path', game_goal_fn)
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'depth_first', 'full', game_goal_fn)
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'breadth_first', 'none', game_goal_fn)
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'breadth_first', 'path', game_goal_fn)
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'breadth_first', 'full', game_goal_fn)
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'astar', 'none', game_goal_fn, heur_min_completion_time)
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'astar', 'path', game_goal_fn, heur_min_completion_time)
    
#     s = make_init_state(size, 0, obstacles_list, player, enemy)
#     test(se, s, 'astar', 'full', game_goal_fn, heur_min_completion_time)