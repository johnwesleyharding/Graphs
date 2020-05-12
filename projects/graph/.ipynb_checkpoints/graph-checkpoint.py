
from util import Stack, Queue


class Gnode:
    
    def __init__(self, data = None):
        
        self.upstream = set()
        self.downstream = set()
        self.data = data


class Graph:

    def __init__(self):
        
        self.vertices = {}

    def add_vertex(self, vertex_id, data = None):
        
        self.vertices[vertex_id] = Gnode(data)

    def add_edge(self, node, target):
        
        if node in self.vertices and target in self.vertices:
            
            self.vertices[node].downstream.add(target)
            self.vertices[target].upstream.add(node)

    def get_neighbors(self, node):
        
        if node in self.vertices:
            
            return self.vertices[node].downstream | self.vertices[node].upstream

    def bft(self, node):
        
        q = Queue()
        visited = set()
        q.enqueue(node)
        
        while q.size() > 0:
            
            n = q.dequeue()
            if n not in visited:
                
                visited.add(n)
                print(n)
                
                for path in self.vertices[n].downstream | self.vertices[n].upstream:

                    q.enqueue(path)

    def dft(self, node):

        s = Stack()
        visited = set()
        s.push(node)
        
        while s.size() > 0:
            
            n = s.pop()
            if n not in visited:
                
                visited.add(n)
                print(n)
                
                for path in self.vertices[n].downstream | self.vertices[n].upstream:

                    s.push(path)
    
    def dft_recursive(self, node, visited = set()):
        
        print(node)
        visited.add(node)
        
        for path in self.vertices[node].downstream | self.vertices[node].upstream:
            
            if path not in visited:

                self.dft_recursive(path, visited)

    def bfs(self, node, target, chain = None):
        
        if chain == None:
            
            chain = [target]
        
        if chain[-1] == node:
            
            return chain[-1::-1]
        
        q = Queue()
        visited = set()
        q.enqueue(node)
        
        while q.size() > 0:
            
            n = q.dequeue()
            
            if target in self.vertices[n].downstream | self.vertices[n].upstream:
                
                chain.append(n)
                return self.bfs(node, chain[-1], chain)
            
            if n not in visited:
                
                visited.add(n)
                
                for path in self.vertices[n].downstream | self.vertices[n].upstream:

                    q.enqueue(path)

    def dfs(self, node, target):
        
        if target == node:
            
            return [node]
        
        c = [[node]]
        visited = {node}
        d = 0
        
        while d > -1:
            
            n = c[d][-1]
            
            if target in self.vertices[n].downstream | self.vertices[n].upstream:
                
                d += 1
                c.append([target])
                chain = [None] * (d + 1)
                
                for i in range(d + 1):

                    chain[i] = c[i][-1]
                
                return chain
            
            flag = False
            d += 1
            c.append([])
            
            for path in self.vertices[n].downstream | self.vertices[n].upstream:

                if path not in visited:

                    c[d].append(path)
                    visited.add(path)
                    flag = True
            
            if flag == False:
                
                c.pop()
                d -= 1
                c[d].pop()
                
                if c[d] == []:

                    c.pop()
                    d -= 1

    def dfs_recursive(self, node, target, chain = [], visited = set()):
        
        visited.add(node)        
        chain.append(node)
        
        if chain[-1] == target:
            
            return chain
        
        for path in self.vertices[node].downstream | self.vertices[node].upstream:
            
            if path not in visited:

                x = self.dfs_recursive(path, target, chain, visited)
            
                if x != None and x[-1] == target:
                
                    return x
                
        chain.pop()
        return chain

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
