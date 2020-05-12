
import sys
sys.path.insert(0, '..\graph')
from graph import Graph, Gnode

def earliest_ancestor(ancestors, node):
    
    g = Graph()
    
    for x, y in ancestors:
        
        if x not in g.vertices:
            
            g.add_vertex(x)
        
        if y not in g.vertices:
            
            g.add_vertex(y)
        
        g.add_edge(y, x)
    
    r = g.bft(node)
    
    if r == node:
        
        return -1
    
    return r
    

# def earliest_ancestor(ancestors, node):
    
#     ht = {}
#     flag = True
    
#     for x, y in ancestors:
        
#         if y in ht:
            
#             ht[y].add(x)
        
#         else:
            
#             ht[y] = {x}
    
#     if node in ht:
        
#         newopts = ht[node]
    
#     else:
        
#         return -1
    
#     while flag:
        
#         options = newopts
#         newopts = set()
#         flag = False
        
#         for o in options:
            
#             if o in ht:
                
#                 flag = True
#                 for n in ht[o]:
                    
#                     newopts.add(n)
        
#     return min(options)
