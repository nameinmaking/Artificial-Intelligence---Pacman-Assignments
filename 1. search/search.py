# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    return search(problem, search_type='dfs', flag=False, star_flag=False, heuristic=nullHeuristic)


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    return search(problem, search_type='bfs', flag=False, star_flag=False, heuristic=nullHeuristic)


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    return search(problem, search_type='us', flag=True, star_flag=False, heuristic=nullHeuristic)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    return search(problem, search_type='astar', flag=True, star_flag=True, heuristic=heuristic)


def search(problem, search_type, flag, star_flag, heuristic):
    # dictionary to allocate correct data strucutres
    structure = {'bfs': util.Queue(), 'dfs': util.Stack(), 'us': util.PriorityQueue(), 'astar': util.PriorityQueue()}
    current_state = problem.getStartState()

    nodes_visited = set()  # a set of visited nodes
    frontier = structure[search_type]

    if flag:  # Uniform and A-Star search
        frontier.push((current_state, [], 0), 0)
    else:  # DFS adn BFS search
        frontier.push((current_state, [], 0))

    while not frontier.isEmpty():
        location, path, cost = frontier.pop()

        if problem.isGoalState(location):  # check for goal state
            return path

        if location not in nodes_visited:
            nodes_visited.add(location)

            if flag and not star_flag:  # DFS and BFS search
                for s_location, s_path, s_cost in problem.getSuccessors(location):
                    if s_location not in nodes_visited:
                        frontier.push((s_location, path + [s_path], s_cost + cost), s_cost + cost)

            if not flag and not star_flag:  # Unifrom cost search
                for s_location, s_path, s_cost in problem.getSuccessors(location):
                    if s_location not in nodes_visited:
                        frontier.push((s_location, path + [s_path], s_cost))

            if star_flag:  # A* search
                for s_location, s_path, s_cost in problem.getSuccessors(location):
                    if s_location not in nodes_visited:
                        backwardCost = s_cost + cost
                        forwardCost = heuristic(s_location, problem)
                        total_cost = backwardCost + forwardCost
                        frontier.push((s_location, path + [s_path], backwardCost), total_cost)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch