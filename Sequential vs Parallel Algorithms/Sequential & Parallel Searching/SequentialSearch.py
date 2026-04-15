def linear_search(data, target):
    for i, value in enumerate(data):
        if value == target:
            return i  # found
    return -1  # not found
target = data[len(data)//2]

index = linear_search(data, target)

print("Sequential Search Result:", index)

