

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


if __name__ == "__main__":
    dll = DoublyLinkedList()

    a = Node("A", 1)
    b = Node("B", 2)
    c = Node("C", 3)

    dll.add_to_front(a)
    dll.add_to_front(b)
    dll.add_to_front(c)

    dll.remove(b)
    last = dll.remove_last()
    
    last = dll.remove_last()
    print(dll.remove_last())

        







        

        



