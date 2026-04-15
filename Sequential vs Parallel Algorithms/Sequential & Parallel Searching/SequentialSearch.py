def linear_search(data, target):
    for i, value in enumerate(data):
        if value == target:
            return i  # return index if found
    return -1  # return -1 if not found

import random
import time

# generate data
data = [random.randint(1, 1000000) for _ in range(100000)]

# choose a target
target = data[len(data)//2]

# measure time
start = time.time()
result = linear_search(data, target)
end = time.time()

print("Index found:", result)
<<<<<<< HEAD
print("Time:", end - start)
=======
print("Time:", end - start)
>>>>>>> 8e90325e71921b062a5e41f2959825424c7708ca
