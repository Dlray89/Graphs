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

def earliest_ancestor(ancestors, starting_node):

    q = Queue()

    curr_node = starting_node
    relationship = {}

    for node in ancestors:
        if node[1] not in relationship:
            relationship[node[1]] = set()
        relationship[node[1]].add(node[0])


    if starting_node in relationship:
        q.enqueue(relationship[curr_node])
        
    else:
        return - 1

    while True:
        relation = q.dequeue()
        curr_node = min(relation)
        if curr_node not in relationship:
            return curr_node
        else:
            q.enqueue(relationship[curr_node])
          