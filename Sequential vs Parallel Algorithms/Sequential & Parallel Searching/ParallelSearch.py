from multiprocessing import Process, Queue

def worker(sub_data, target, q, offset):
    for i, value in enumerate(sub_data):
        if value == target:
            q.put(i + offset)  # global index
            return
    q.put(-1)


def parallel_search(data, target):
    q = Queue()
    processes = []
    num_processes = 4

    chunk_size = len(data) // num_processes

    for i in range(num_processes):
        start = i * chunk_size
        end = len(data) if i == num_processes - 1 else (i + 1) * chunk_size

        p = Process(target=worker, args=(data[start:end], target, q, start))
        processes.append(p)
        p.start()

    results = [q.get() for _ in processes]

    for p in processes:
        p.join()

    valid_results = [res for res in results if res != -1]
    return min(valid_results) if valid_results else -1


# REQUIRED for Windows multiprocessing
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    target = data[len(data)//2]

    index = parallel_search(data, target)
    print("Parallel Search Result:", index)