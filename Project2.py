'''
Project 2
'''

def bfs_visited(ugraph, start_node):
    '''
    Takes the undirected graph (ugraph) and the node 
    (start_node) and returns the set consisting of
    all nodes that are visited by a breadth-first search
    that starts at start_node.
    '''
    visited = {start_node}
    queue = []
    
    queue.append(start_node)
    while len(queue) > 0:
        i = queue.pop(0)
        for value in ugraph[i]:
            if value not in visited:
                visited.add(value)
                queue.append(value)
    return visited
    
def cc_visited(ugraph):
    '''
    Takes the undirected graph (ugraph)
    and returns a list of sets, where 
    each set consists of all the nodes 
    (and nothing else) in a connected
    component, and there is exactly one 
    set in the list for each connected 
    component in ugraph and nothing else.
    '''

    remaining_nodes = ugraph.keys()
    connected_components = []
    
    while len(remaining_nodes) > 0:
        visited = bfs_visited(ugraph,remaining_nodes[0])
        connected_components.append(visited)
        for node in visited:
            remaining_nodes.remove(node)
    return connected_components

def largest_cc_size(ugraph):
    '''
    Takes the undirected graph (ugraph) 
    and returns the size (an integer) of 
    the largest connected component in ugraph.
    '''
    
    connected_components = cc_visited(ugraph)
    largest_size = 0
    
    for node in connected_components:
        if len(node) > largest_size:
            largest_size = len(node)
    return largest_size

def compute_resilience(ugraph, attack_order):
    '''
    Takes the undirected graph (ugraph)
    and returns the size (an integer) of
    the largest connected component in ugraph
    after each attack from the list (attack_order)
    '''
    resilience = [largest_cc_size(ugraph)]
        
    for node in attack_order:
        removed = ugraph.pop(node)
        for edge in removed:
            ugraph[edge].discard(node)
        resilience.append(largest_cc_size(ugraph))
    return resilience  