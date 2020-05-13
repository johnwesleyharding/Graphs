
import numpy as np


class User:
    
    def __init__(self, name):
        
        self.name = name
        

class SocialGraph:
    
    def __init__(self):
        
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):

        if user_id == friend_id:
            
            print("WARNING: You cannot be friends with yourself")
            
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            
            print("WARNING: Friendship already exists")
            
        else:
            
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)            

    def add_user(self, name):

        self.last_id += 1
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):

        if num_users <= avg_friendships:
            
            return 'too many friends per user'
        
        self.last_id = 0
        self.users = {}
        self.friendships = {}        
        
        for n in range(num_users):
            
            self.add_user(f'person{n}')
        
        size = (num_users * avg_friendships) // 2
        friends = np.random.randint(1, self.last_id + 1, size = (size * 2, 2))
        count, i = 0, 0
        
        while count < size:
            
            ship = friends[i]
            if ship[0] != ship[1] and ship[1] not in self.friendships[ship[0]]:
                
                self.add_friendship(ship[0], ship[1])
                count += 1
            
            i += 1

    def get_all_social_paths(self, user_id):
        
        visited = {user_id: [user_id]}
        current = {user_id: sg.friendships[user_id]}
        flag = True
        
        while flag:
            
            degree = {}
            flag = False
            
            for friend in current:
                
                for path in current[friend]:
                
                    if path not in visited:
                        
                        visited[path] = visited[friend][:]
                        visited[path].append(path)
                        degree[path] = sg.friendships[path]
                        flag = True
            
            current = degree
        
        visited.pop(user_id)
        return visited
    

if __name__ == '__main__':
    
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
    
    sg = SocialGraph()
    sg.populate_graph(1000, 5)
    connections = sg.get_all_social_paths(1)
    print(f'percent of graph in network: {len(connections) / 9.99:.2f} %')
    total = 0
    for friend in connections:
        total += len(connections[friend]) - 1
    print(f'average degree of separation {total / len(connections):.2f}')
