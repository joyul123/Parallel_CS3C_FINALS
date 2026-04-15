import random
import time
from multiprocessing import Pool
import heapq

#merge sort
def parallelSort(nums):
    if len(nums) > 1:
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]

        #recursion
        parallelSort(left)
        parallelSort(right)

        #merge
        i = 0 
        j = 0 
        k = 0 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1
        while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1
    return nums

small = [random.randint(1, 1000) for _ in range(10)]
#medium = [random.randint(1, 100000) for _ in range(10)]
#large = [random.randint(1, 1000000) for _ in range(10)]

reverseSorted = sorted(small, reverse=True)

chunk_size = len(reverseSorted) // 4

chunks = [reverseSorted[i:i + chunk_size] for i in range(0, len(reverseSorted),
chunk_size)]

start = time.perf_counter()

with Pool(4) as p:
    sorted_chunks = p.map(parallelSort, chunks)

mergedChunks = list(heapq.merge(*sorted_chunks))

print(mergedChunks)

end = time.perf_counter()

print(f'total time: {end - start:.6f}')

