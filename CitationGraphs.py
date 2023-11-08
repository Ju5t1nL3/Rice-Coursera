"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports
import math
import urllib2
import simpleplot
import codeskulptor
codeskulptor.set_timeout(20)

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"
def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph


citation_graph = load_graph(CITATION_URL)

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

print in_degree_distribution(citation_graph)

TOTAL_NODES = 27770

def normalized_distribution(digraph,total_nodes):
    '''
    Takes a directed graph(digraph - represented as 
    a dictionary) and the number of nodes (total_nodes)
    and computes the normalized distribution of the 
    in-degrees of the graph that sums up to 1
    '''
    
    new_graph = {}
    
    unnormalized = in_degree_distribution(digraph)
    
    for frequency in unnormalized.keys():
        new_graph[frequency] = float(unnormalized[frequency])/total_nodes
    return new_graph


normal = normalized_distribution(citation_graph,TOTAL_NODES)

print normal

def convert_to_log(digraph):
    '''
    takes the graph and turns both the keys and values
    into log so that it becomes a log/log graph
    '''
    
    new_graph = {}
    
    for key in digraph:
        if key != 0:
            new_graph[math.log(key,10)] = math.log(digraph[key],10)
    return new_graph

log_data = convert_to_log(normal)

print log_data

simpleplot.plot_scatter('Sample', 800, 600, 'x', 'y', [log_data])







