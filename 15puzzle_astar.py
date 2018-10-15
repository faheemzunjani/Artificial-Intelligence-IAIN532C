import sys

goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def display_board( state ):
    print ("------------------")
    print ("| %i | %i | %i | %i |" % (state[0], state[4], state[8], state[12]))
    print ("------------------")
    print ("| %i | %i | %i | %i |" % (state[1], state[5], state[9], state[13]))
    print ("------------------")
    print ("| %i | %i | %i | %i |" % (state[2], state[6], state[10], state[14]))
    print ("------------------")
    print ("| %i | %i | %i | %i |" % (state[3], state[7], state[11], state[15]))
    print ("------------------")

def move_up( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [0, 4, 8, 12]:
        new_state[index - 1], new_state[index] = new_state[index], new_state[index - 1]
        return new_state
    else:
        return None

def move_down( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [3, 7, 11, 15]:
        new_state[index +1], new_state[index] = new_state[index], new_state[index +1]
        return new_state
    else:
        return None

def move_left( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [0, 1, 2, 3]:
        new_state[index -4], new_state[index] = new_state[index], new_state[index -4]
        return new_state
    else:
        return None

def move_right( state ):
    new_state = state[:]
    index = new_state.index( 0 )
    if index not in [12, 13, 14, 15]:
        new_state[index +4], new_state[index] = new_state[index], new_state[index +4]
        return new_state
    else:
        return None

def create_node( state, parent, operator, depth, cost ):
    return Node( state, parent, operator, depth, cost )

def expand_node( node, nodes ):
    expanded_nodes = []
    expanded_nodes.append( create_node( move_up( node.state ), node, "u", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_down( node.state ), node, "d", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_left( node.state ), node, "l", node.depth + 1, 0 ) )
    expanded_nodes.append( create_node( move_right( node.state), node, "r", node.depth + 1, 0 ) )
    expanded_nodes = [node for node in expanded_nodes if node.state != None] #list comprehension!
    return expanded_nodes

def cmp( x, y ):
    # Compare function for A*. f(n) = g(n) + h(n). I use depth (number of moves) for g().
    return (x.depth + h( x.state, goal_state )) - (y.depth + h( x.state, goal_state ))

def a_star( start, goal ):

    nodes = []
    nodes.append( create_node( start, None, None, 0, 0 ) )
    while True:
        # We've run out of states - no solution.
        if len( nodes ) == 0: return None
        # Sort the nodes with custom compare function.
        nodes.sort( cmp )
        # take the node from the front of the queue
        node = nodes.pop(0)
        # if this node is the goal, return the moves it took to get here.
        print ("Expanded state", display_board(node.state), " using move: ", node.operator)
        if node.state == goal:
            moves = []
            temp = node
            while True:
                moves.insert( 0, temp.operator )
                if temp.depth <=1: break
                temp = temp.parent
            return moves
        # Expand the node and add all expansions to the end of the queue
        nodes.extend( expand_node( node, nodes ) )


def h( state, goal ):
    """Heuristic for the A* search. Returns an integer based on out of place tiles"""
    """Hamming distance used"""
    score = 0
    for i in range( len( state ) ):
        if state[i] != goal[i]:
            score = score + 1
    return score

# Node data structure
class Node:
    def __init__( self, state, parent, operator, depth, cost ):
        # Contains the state of the node
        self.state = state
        # Contains the node that generated this node
        self.parent = parent
        # Contains the operation that generated this node from the parent
        self.operator = operator
        # Contains the depth of this node (parent.depth +1)
        self.depth = depth
        # Contains the path cost of this node from depth 0. Not used for depth/breadth first.
        self.cost = cost

def main():
    starting_state = [4,0,2,3,5,1,6,7,8,9,10,11,12,13,14,15]
    
    print ("Start state")
    
    result = a_star( starting_state, goal_state )
    if result == None:
        print ("No solution found")
    elif result == [None]:
        print ("Start node was the goal!")
    else:
        print (result)
        print ("Total moves: ", len(result))

main()