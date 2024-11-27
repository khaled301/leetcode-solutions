class Heap:
    def __init__(self, heap):
        self.heap = heap
        self.size = len(heap)
    
    def getHeap(self):
        return self.heap
    
    def getLeftChildIndex(self, parentIndex):
        return (2 * parentIndex) + 1
    
    def getRightChildIndex(self, parentIndex):
        return (2 * parentIndex) + 2
    
    def getParentIndex(self, childIndex):
        return (childIndex - 1) // 2
    
    def getLastParentNodeIndex(self):
        return (self.size // 2) - 1
    
    def hasLeftChild(self, index):
        tempIndex = self.getLeftChildIndex(index)
        return tempIndex >= 0 and tempIndex < self.size
    
    def hasRightChild(self, index):
        tempIndex = self.getRightChildIndex(index)
        return tempIndex  >= 0 and tempIndex < self.size
    
    def hasParent(self, index):
        tempIndex = self.getParentIndex(index)
        return tempIndex >= 0 and tempIndex < self.size
    
    def leftChild(self, index):
        return self.heap[self.getLeftChildIndex(index)] if self.hasLeftChild(index) else None
    
    def rightChild(self, index):
        return self.heap[self.getRightChildIndex(index)] if self.hasRightChild(index) else None
    
    def parent(self, index):
        return self.heap[self.getParentIndex(index)] if self.hasParent(index) else None
    
    def swap(self, index1, index2):
        if index1 == index2:
            return 
        
        if index1 < 0 or index1 >= self.size or index2 < 0 or index2 >= self.size:
            raise Exception("Invalid indices")
        
        # self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
        
    def peek(self):
        return self.heap[0] if self.size > 0 else None
    
    def poll(self):
        if self.size < 1:
            raise Exception("Heap is empty")
        
        item = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.size -= 1
        
        self.minHeapifyDown()
        
        return item
    
    def add(self, item):
        self.heap.append(item)
        self.size += 1
        self.minHeapifyUp()

    def minHeapifyUp(self):
        tempIndex = self.size - 1
        while self.hasParent(tempIndex) and self.parent(tempIndex) > self.heap[tempIndex]:
            self.swap(self.getParentIndex(tempIndex), tempIndex)
            tempIndex = self.getParentIndex(tempIndex)

    def minHeapifyDown(self):
        # root node is at index 0
        tempIndex = 0
        while self.hasLeftChild(tempIndex):
            smallerChildIndex = self.getLeftChildIndex(tempIndex)
            
            if self.hasRightChild(tempIndex) and self.rightChild(tempIndex) < self.leftChild(tempIndex):
                smallerChildIndex = self.getRightChildIndex(tempIndex)
    
            if self.heap[tempIndex] < self.heap[smallerChildIndex]:
                break
            else:
                self.swap(tempIndex, smallerChildIndex)
                
            tempIndex = smallerChildIndex


if __name__ == "__main__":
    heap = Heap([3, 2, 1, 5, 6, 4])
    heap.minHeapifyDown()
    print(heap.getHeap())
    
    print(heap.peek())
    print(heap.poll())
    print(heap.getHeap())
    print(heap.peek())
    heap.add(18)
    print(heap.peek())
    print(heap.getHeap())
    
    
    print(heap.hasParent(2))
    print(heap.hasLeftChild(1))
    print(heap.hasRightChild(3))