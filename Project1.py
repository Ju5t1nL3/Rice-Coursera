EX_GRAPH0 = {0:set([1,2]), 1:set([]), 2:set([])}

EX_GRAPH1 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3]), 3:set([0]), 4:set([1]), 5:set([2]), 6:set([])}

EX_GRAPH2 = {0:set([1,4,5]), 1:set([2,6]), 2:set([3,7]), 3:set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    '''
    Takes the number of nodes (num_nodes) and 
    returns a dictionary corresponding to a 
    complete directed graph with the specified 
    number of nodes
    '''
    
    if num_nodes > 0:
        complete_graph = {}
        
        all_nodes = [n for n in range(num_nodes)]
        
        for node in range(num_nodes):
            complete_graph[node] = set()
            for edge in all_nodes:
                if edge != node:
                    complete_graph[node].add(edge)
        
        return complete_graph
        
    else: 
        return {}
    
def compute_in_degrees(digraph):
    '''
    Takes a directed graph (digraph - represented as 
    a dictionary) and computes the in-degrees for the 
    nodes in the graph
    '''
    
    new_graph = {}
        
    for node in digraph: 
        new_graph[node] = 0
    for node in digraph: 
        for value in digraph[node]:
            new_graph[value] += 1
    
    return new_graph

def in_degree_distribution(digraph):
    '''
    Takes a directed graph(digraph - represented as 
    a dictionary) and computes the unnormalized 
    distribution of the in-degrees of the graph
    '''
    
    new_graph = {}
    
    in_degrees = compute_in_degrees(digraph)
    
    for value in in_degrees.values():
        if value not in new_graph.keys():
            new_graph[value] = 0
        new_graph[value] += 1
            
    return new_graph
