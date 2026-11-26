

class Node:

    def __init__(self, key, value):
        self.key = key # for url id
        self.value = value # for long url
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        # sentinel nodes to sit at each end
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    
    def add_to_front(self, node):
        old_first_node = self.head.next 
        
        node.prev = self.head
        node.next = old_first_node
        self.head.next = node
        old_first_node.prev = node

    
    def remove_last(self):
        last_node = self.tail.prev
        if last_node is self.head:
            return None

        self.remove(last_node)
        
        return last_node

    
    def _to_list(self):
        collected_keys = []
        current = self.head.next

        while current is not self.tail:
            collected_keys.append(current.key)
            current = current.next # to move onto the next node

        return collected_keys

# dict storing the nodes, since no matter what a dict lookup is one step, and moving the object(node) around is fewer pointer changes
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity # max # of entries
        self.map = {} # key to node dict
        self.order = DoublyLinkedList() # new dll obj
        self.hits = 0
        self.misses = 0

    
    def _move_to_front(self, node): # helper
        self.order.remove(node)
        self.order.add_to_front(node)


    def get(self, key): # since we're grabbing the value, it has to be marked as just used 
        # has to be moved to front (reading entry counts as using it)
        if key not in self.map:
            self.misses += 1
            return None

        node = self.map[key] # grab node from dict
        self._move_to_front(node)
        self.hits += 1
        
        return node.value

    
    def put(self, key, value): # to add or update existing one
        if key in self.map:
            node = self.map[key] # get its node
            node.value = value # to match the parameter
            # move to front 
            self._move_to_front(node)

        else:
            node = Node(key, value)
            self.map[key] = node
            self.order.add_to_front(node)
            

        if len(self.map) > self.capacity:
            oldest_node = self.order.remove_last()
            del self.map[oldest_node.key]



if __name__ == "__main__":
    # test zone 
    pass

        







        

        



