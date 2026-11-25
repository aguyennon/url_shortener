

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
        
        if node:
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
        self.capacity = 2 # max # of entries
        self.map = {} # key to node dict
        self.order = DoublyLinkedList() # new dll obj

    
    def get(self, key): # since we're grabbing the value, it has to be marked as just used 
        # has to be moved to front (reading entry counts as using it)
        if key not in self.map:
            return None
        else:
            node = self.map[key] # grab node from dict
            removed_node = self.order.remove(node)
            node_to_front = self.order.add_to_front(removed_node)
        
        return node.value

    
    def put(self, key, value): # to add or update existing one
        if key in self.map:
            node = self.map[key] # get its node
            node.value = value # to match the parameter
            # move to front 
            removed_node = self.order.remove(node)
            node_to_front = self.order.add_to_front(removed_node)

        elif key not in self.map:
            self.map[key] = Node(key, value)
            node_to_front = self.order.add_to_front(self.map[key])

        if len(self.map) > self.capacity:
            oldest_node = self.order.remove_last()
            del self.map[oldest_node.key]




if __name__ == "__main__":
    lru = LRUCache(capacity=2)


    lru.put("A", 100)
    lru.put("C", 3)

    print(len(lru.map))

        







        

        



