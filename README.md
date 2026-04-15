# Parallel_CS3C
# Sequential vs Parallel Algorithms 

Aaron Adanza
● Differences observed between sequential and parallel execution 
● Performance behavior across dataset sizes 
● Challenges encountered during implementation 
● Insights about overhead, synchronization, or merging 
● Situations where parallelism was beneficial or unnecessary 

Ced Louise Bentuzal
● Differences observed between sequential and parallel execution 
● Performance behavior across dataset sizes 
● Challenges encountered during implementation 
● Insights about overhead, synchronization, or merging 
● Situations where parallelism was beneficial or unnecessary 


Mitch Dumdum
● Differences observed between sequential and parallel execution 
● Performance behavior across dataset sizes 
● Challenges encountered during implementation 
● Insights about overhead, synchronization, or merging 
● Situations where parallelism was beneficial or unnecessary 


Niros Val Inojales
● Differences observed between sequential and parallel execution 
● Performance behavior across dataset sizes 
● Challenges encountered during implementation 
● Insights about overhead, synchronization, or merging 
● Situations where parallelism was beneficial or unnecessary 


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