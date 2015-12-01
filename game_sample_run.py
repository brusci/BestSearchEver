from game import *

if __name__ == '__main__':
    s = make_init_state(10, 0, [], [5, 5], [2, 2])
    se = SearchEngine('astar', 'full')
#     se.search(s, warehouse_goal_fn, heur_min_completion_time)
    se.set_strategy('breadth_first')
    se.search(s, game_goal_fn)
