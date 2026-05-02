CS321_CS3C 
![Alt text](https://github.com/joyul123/Parallel_CS3C_FINALS/blob/main/CS_321_CS3C_MEMBERS.png?raw=true)













# Parallel_CS3C
# Sequential vs Parallel Algorithms 

Aaron Adanza
● Differences observed between sequential and parallel execution
Sequential runs step-by-step using one process, while parallel execution splits the task into chunks and runs them at the same time using multiple processes. Parallel is more complex but can use multiple CPU cores.

● Performance behavior across dataset sizes
For small datasets, sequential was faster due to low overhead. For medium and large datasets, parallel became more efficient and showed better performance as workload increased.

● Challenges encountered during implementation
Difficulties included splitting data correctly, managing multiple processes, and combining results properly. In searching, returning the correct global index was also challenging.

● Insights about overhead, synchronization, or merging
Parallel processing has overhead from creating processes and communication. Synchronization is needed when collecting results, and merging sorted chunks correctly is important to maintain accuracy.

● Situations where parallelism was beneficial or unnecessary
Parallelism was beneficial for large datasets where the workload is heavy. It was unnecessary for small datasets because the overhead made it slower than sequential execution.


Mitch Dumdum
● Differences observed between sequential and parallel execution 
Sequential Execution is the completion of a task one after the next in a specific order of execution. This makes our task of debugging simple. In contrast, Parallel Execution breaks a task into smaller pieces and runs them all at once with multiple parallel processes. While this helps to use resources effectively, it introduces complexity; you have to manage coordination, synchronization, and proper data handling for all of the tasks that are executed in parallel.

● Performance behavior across dataset sizes 
Smaller-sized datasets worked better using a sequential algorithm because there was very slight overhead associated with a sequential algorithm's execution. Conversely, larger datasets required the use of efficient parallel algorithms to allow the distribution of work across multiple processors. The performance gain of a parallel algorithm is not as reliable sometimes due to overhead that can impact execution times.

● Challenges encountered during implementation 
The difficulty of dividing the dataset correctly, as well as having each process carry out its assigned phase correctly, was one of the most challenging aspects of working with parallel data. Merging sorted chunks back together in parallel sorting and getting a global index in parallel searching have also proven to be challenging. Finally, troubleshooting parallel code has become far more difficult owing to having so many processes running simultaneously.

● Insights about overhead, synchronization, or merging 
In parallel algorithms, there are some performance detriments that arise from such things as creating processes, communicating between them, and context switching. Furthermore, synchronizing for correctness can cause execution delay if done poorly. Merging of results may also become a bottleneck if it is not efficiently implemented.

● Situations where parallelism was beneficial or unnecessary 
For tasks with large datasets, using parallelism increased performance because all tasks could be processed at the same time, however, for small datasets using parallelism is not necessary and more overhead was incurred than if they would have been executed sequentially making sequential execution faster than the use of parallelism in the majority of these types of situations.


Niros Val Inojales
● Differences observed between sequential and parallel execution 
Answer: The main difference is how your computer's brain tackles a job. Sequential execution is like a single-lane road: it follows one path, finishing one task before starting the next. It is simple and predictable with very little paperwork, but it’s limited by the speed of a single processor core. Parallel execution is more like a multi lane highway. It breaks a big task into smaller chunks so that multiple processor cores can work on them at the exact same time. While this is much faster for massive datasets, it adds extra work because the computer has to spend time creating processes and coordinating how to merge all the pieces back together. You'll often find that for small tasks, the sequential way is actually faster because it avoids all that extra management.

● Performance behavior across dataset sizes
Answer: The performance of these algorithms changes significantly based on the amount of data they are processing. For a Small Dataset of 1,000 elements, sequential algorithms typically perform better because they have low overhead and do not require the extra time needed for process creation or synchronization. However, as you move to a Medium Dataset of 100,000 elements, you reach a tipping point where the computational workload begins to outweigh the coordination costs. By the time you reach a Large Dataset of 1,000,000 elements, parallel algorithms clearly demonstrate their scalability potential, utilizing multiple CPU cores to handle the massive workload simultaneously. Ultimately, while sequential speed is limited by the efficiency of a single core, parallel execution becomes much more beneficial as the data grows large enough to justify the complexity of managing multiple processes.

● Challenges encountered during implementation 
Answer: One of the biggest hurdles was data partitioning, which requires precisely dividing the dataset into chunks and ensuring the last process handles any remainder. In parallel searching, it was challenging to calculate the correct global index, as each process only knows its position within its own small slice of data. For sorting, the main difficulty lay in the merging and synchronization phase, where individual sorted chunks must be combined into one final list without creating a performance bottleneck. Finally, managing interprocess communication through queues required careful coordination to ensure results were resolved correctly from all simultaneous workers.

● Insights about overhead, synchronization, or merging 
Answer: A key insight is that parallel algorithms aren't always faster because they require extra management that sequential models avoid. Overhead the time the system spends creating processes and handling communication can actually make parallel execution slower than sequential for small tasks. Synchronization is also essential to ensure correctness, such as merging partitioned results or avoiding race conditions. Finally, merging acts as a potential bottleneck; while chunks are sorted quickly in parallel, combining them into one global list requires careful coordination to keep the performance gains. Parallelism is essentially a trade off where you gain scalability at the cost of higher complexity and coordination.

● Situations where parallelism was beneficial or unnecessary 
Answer: Parallelism was unnecessary for small datasets, like the 1,000 element test, because the overhead the time the computer spends creating processes and managing communication took longer than the actual task itself. In these cases, a sequential approach is more efficient because it avoids all management costs. However, parallelism was highly beneficial for the large dataset of 1,000,000 elements. At this scale, the massive workload outweighs the coordination costs, allowing the algorithm to take full advantage of multiple CPU cores to finish the job much faster. Ultimately, parallelism is a tool meant for heavy lifting; using it for small, simple tasks is often slower and less efficient than sticking to a single linear path.


Ced Louise R. Bentuzal Reflection
● Differences observed between sequential and parallel execution
Sequential execution processes tasks one after another, making it simpler and more predictable. Parallel execution runs multiple tasks simultaneously, which can significantly reduce processing time but introduces added complexity like synchronization and coordination.

● Performance behavior across dataset sizes
For small datasets, parallel execution often shows little to no improvement due to overhead. As dataset size increases, parallel processing becomes more efficient and can outperform sequential execution by utilizing multiple cores.

● Challenges encountered during implementation
Managing threads or processes, handling race conditions, and ensuring proper data sharing were common challenges. Debugging parallel code was also more difficult compared to sequential logic.

● Insights about overhead, synchronization, or merging
Parallel systems introduce overhead from thread creation, communication, and synchronization. Improper handling of shared resources can lead to delays, and merging results from parallel tasks can sometimes offset performance gains.

● Situations where parallelism was beneficial or unnecessary
Parallelism was beneficial for large, independent tasks that could be divided evenly. However, it was unnecessary or inefficient for small workloads or tasks with heavy dependencies between steps.


Sophia Plariza
● Differences observed between sequential and parallel execution

Answer: Sequential execution processes data step-by-step using a single control flow, which makes it simple, predictable, and easier to debug. In contrast, parallel execution divides the task into multiple smaller parts that run simultaneously across multiple processes. While parallel algorithms can significantly reduce execution time, they are more complex due to the need for coordination, communication, and synchronization between processes.

● Performance behavior across dataset sizes 

Answer: During testing, sequential algorithms performed better on small datasets because they have minimal overhead. The parallel versions were slower in these cases due to the cost of creating processes and managing communication. However, as the dataset size increased (especially at 100,000 and 1,000,000 elements), parallel algorithms showed improved performance. The benefit became more noticeable when the workload was large enough to outweigh the overhead of parallelization.

● Challenges encountered during implementation 

Answer: One of the main challenges was implementing multiprocessing correctly, especially in dividing the dataset and ensuring that each process handled its assigned portion properly. Another difficulty was merging sorted chunks in the parallel sorting algorithm while maintaining correctness. In parallel searching, handling the global index and collecting results from multiple processes using queues required careful design. Debugging was also more difficult compared to sequential code.

● Insights about overhead, synchronization, or merging 

Answer: Parallel algorithms introduce overhead such as process creation, context switching, and inter-process communication. Synchronization is necessary to ensure that all processes complete correctly and to avoid issues like race conditions. In parallel sorting, merging results from different processes adds additional cost, which can reduce the overall performance gain. These factors show that parallelism is not always efficient and must be used carefully.

● Situations where parallelism was beneficial or unnecessary 

Answer: Parallelism was beneficial when working with large datasets because it utilized multiple CPU cores and reduced execution time. However, for small datasets, parallel execution was unnecessary and even slower due to overhead costs. Therefore, sequential algorithms are more suitable for small-scale problems, while parallel algorithms are better for large-scale computations where performance improvements justify the added complexity.

