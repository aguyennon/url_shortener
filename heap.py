


class MinHeap:
    
    def __init__(self):
        self.items = []

    
    def push(self, item):
        self.items.append(item)
        i = len(self.items) - 1 # set i to the index of the item just added (would be last index in list)
        parent = (i - 1) // 2 # formula to find its parent index

        while i > 0 and self.items[i] < self.items[parent]: # i smaller than the item at its parent index
            # swap to set i to the parent index, that way first is always the smallest item
            self.items[i], self.items[parent] = self.items[parent], self.items[i] 
            i = parent
            parent = (i - 1) // 2 # to work out the parent of the new position




if __name__ == "__main__":
    heap = MinHeap()

    heap.push(5)
    print(heap.items[0])
    heap.push(1)
    print(heap.items[0])
    heap.push(9)
    print(heap.items[0])
    heap.push(3)
    print(heap.items[0])
    heap.push(7)
    print(heap.items[0])
    heap.push(2)
    print(heap.items[0])
    print(len(heap.items))
    print(heap.items)

