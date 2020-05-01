
def earliest_ancestor(ancestors, starting_node):
    neighbors_to_visit = Queue()
    neighbors_to_visit.enqueue([starting_node])
    longest_path = []
    visited = set()

    while neighbors_to_visit.size() > 0:
        path = neighbors_to_visit.dequeue()
        v = path[-1]

        if v not in visited:
            visited.add(v)

        if len(path) > len(longest_path):
            longest_path = path
        
        for i in range(len(ancestors)):

            if ancestors[i][1] is v:
                new_path = path.copy()
                new_path.append(ancestors[i][0])
                neighbors_to_visit.enqueue(new_path)
        print('longest_path', longest_path)

        
    earliest = longest_path.pop()
    
    if earliest is starting_node:
        earliest = -1
    elif len(path) == len(longest_path):
            if path[-1] < longest_path[-1]:
                longest_path = path 
    return earliest



class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)