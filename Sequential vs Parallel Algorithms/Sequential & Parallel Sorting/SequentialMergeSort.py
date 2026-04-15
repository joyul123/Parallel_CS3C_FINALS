import random
import time

#merge sort
def parallelSort(nums):
    if len(nums) > 1:
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2:]

        #recursion
        parallelSort(left)
        parallelSort(right)

        #merge
        i = 0 # left index
        j = 0 # right index
        k = 0 # merge index
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


small = [random.randint(1, 1000) for _ in range(10)]
#medium = [random.randint(1, 100000) for _ in range(10)]
#large = [random.randint(1, 1000000) for _ in range(10)]

reverseSorted = sorted(small, reverse=True)

start = time.perf_counter()

parallelSort(small)
print(small)
#parallelSort(medium)
#print(medium)
#parallelSort(large)
#print(large)

end = time.perf_counter()

print(f'total time: {end - start:.6f}')