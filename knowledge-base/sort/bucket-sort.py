"""
    Bucket Sort is a comparison sort algorithm that distributes elements 
    into a number of buckets. Each bucket is then sorted individually, 
    either using a different sorting algorithm or by recursively applying 
    the bucket sort algorithm. It’s particularly useful for sorting numbers 
    that are uniformly distributed over a range.

    Steps of Bucket Sort
    1) Create Buckets: 
    Create an array of empty buckets.

    2) Distribute Elements: 
    Go through the original array, 
    putting each element into its respective bucket based on some criteria.

    3) Sort Buckets: 
    Sort each non-empty bucket. 
    We can use a different sorting algorithm (like Insertion Sort) for this step.

    4) Concatenate Buckets: 
    Combine the sorted buckets into a single array to get the final sorted array.
"""
class CustomSort:
    def __init__(self, arr):
        self.data = arr 
        self.size = len(arr)
        
    def bucketSort(self):
        # create empty buckets
        buckets = [[] for _ in range(self.size + 1)]
        # print(buckets)
        
        # Putting elements into respective buckets
        maxValue = max(self.data)
        for item in self.data:
            # normalize item to fit into the bucket range
            index = int(self.size * item / (maxValue + 1)) 
            buckets[index].append(item)
            
        # Sort each non-empty buckets
        for bucket in buckets:
            if bucket and len(bucket) > 1:
                bucket.sort()
                
        # Concatenate buckets
        result = []
        for bucket in buckets:
            if bucket:
                result.extend(bucket)
                
        return result 
    
if __name__ == "__main__":
    # array = [3, 6, 8, 10, 1, 2, 1]
    array = [0.22, 0.45, 0.12, 0.39, 0.88, 0.29, 0.33, 0.01]
    customSort = CustomSort(array)
    sortedArray = customSort.bucketSort()
    print("Sorted array:", sortedArray)