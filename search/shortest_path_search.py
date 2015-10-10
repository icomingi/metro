# -*- coding: utf-8 -*-

def shortest_path_search(start, is_goal, successors):
    Fail = []
    if is_goal(start):
        return [ start ]
    explored = set()
    frontier = [ [ start ] ]
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for state, action in successors[s].items():
            if state not in explored:
                explored.add(state)
                path2 = path + [ action, state ]
                if is_goal(state):
                    return path2
                frontier.append(path2)
    return Fail

def lowest_cost_search(start, is_goal, successors, action_cost):
     Fail = []
     if is_goal(start):
          return [ start ]
     explored = set()
     frontier = [ [ start ] ] ## Could be replaced by a PriorityQueue
     while frontier:
          path = frontier.pop(0)
          action1, state1 = final_action_state(path)
          if is_goal(state1):
               return path
          pcost = path_cost(path)
          for state, action in successors(state1).items():
               if state not in explored:
                    explored.add(state)
                    path2 = path + [ (action, pcost + action_cost(action1, state1, action, state)), state ]
                    frontier.append(path2)
                    frontier.sort(key=path_cost)
     return Fail

def final_action_state(path):
    "return the final state from a path"
    if len(path) > 1
         return path[-2][0], path[-1]
    return None, path[-1]

def path_cost(path):
    "return the cost of a path"
    if len(path) > 1:
         return path[-2][-1]
    return 0
