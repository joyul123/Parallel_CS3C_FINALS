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

