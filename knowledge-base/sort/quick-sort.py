class CustomSort:
    def __init__(self):
        pass
        
    def quickSort(self, arr):
        # print(f"Arr: {arr}")
        
        # already sorted
        if len(arr) <= 1:
            return arr
        
        pivot = arr[-1]
        
        left = [leftItem for leftItem in arr[:-1] if leftItem <= pivot]
        right = [rightItem for rightItem in arr[:-1] if rightItem > pivot]
        
        # print(f"Left Arr: {left}")
        # print(f"Right Arr: {right}")
        
        sortedLeft = self.quickSort(left) if len(left) > 1 else left
        sortedRight = self.quickSort(right) if len(right) > 1 else right
        
        return sortedLeft + [pivot] + sortedRight
    
    def quickSortInPlace(self, arr, low, high):
        # print(f"Arr: {arr}, low: {low}, high: {high}")
        
        if low < high:
            pi = self.partitioning(arr, low, high) 
            # print(f"PI: {pi}")
            # print(f"Arr: {arr}, low: {low}, high: {high}")
            # print('-' * 50)
            
            self.quickSortInPlace(arr, low, pi - 1)
            self.quickSortInPlace(arr, pi + 1, high)
            
        return arr
    
    def partitioning(self, arr, low, high):
        pivot, p = arr[high], low
        
        for i in range(low, high):
            if arr[i] <= pivot:
                arr[p], arr[i] = arr[i], arr[p]
                p += 1
        arr[p], arr[high] = arr[high], arr[p]
    
        return p

if __name__ == "__main__":
    array = [3, 6, 8, 10, 1, 2, 1]
    customSort = CustomSort()
    # sortedArray = customSort.quickSort(array)
    sortedArray = customSort.quickSortInPlace(array, 0, len(array) - 1)
    print("Sorted array:", sortedArray)