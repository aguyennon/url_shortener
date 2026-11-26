


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

    
    def pop(self):
        if not self.items:
            return None
        
        smallest_item = self.items[0]
        last_item = self.items.pop(-1) # remove last item so the list isnt affected

        if not self.items:
            return smallest_item # if thats all the list had then return it
        # otherwise put last item at index 0
        self.items[0] = last_item

        i = 0
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            smallest = i
            if left_child < len(self.items) and self.items[left_child] < self.items[smallest]:
                smallest = left_child
            if right_child < len(self.items) and self.items[right_child] < self.items[smallest]:
                smallest = right_child
            if smallest == i: # if still smallest than both children break
                break
            # otherwise, swap
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            i = smallest
        
        return smallest_item



if __name__ == "__main__":
    heap = MinHeap()

    heap.push(5)
    heap.push(1)
    heap.push(9)
    heap.push(3)
    heap.push(7)
    heap.push(2)
    while heap.items:
        print(heap.pop(), heap.items)

    

