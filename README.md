# Parallel_CS3C
# Sequential vs Parallel Algorithms 

● Differences observed between sequential and parallel execution 
● Performance behavior across dataset sizes 
● Challenges encountered during implementation 
● Insights about overhead, synchronization, or merging 
● Situations where parallelism was beneficial or unnecessary 

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


