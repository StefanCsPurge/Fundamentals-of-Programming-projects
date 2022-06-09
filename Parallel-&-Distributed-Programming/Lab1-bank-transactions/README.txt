
Threading - Bank accounts app documentation
-------------------------------------------

1. There are independent operations, that operate on shared data.
2. There are several threads launched at the beginning, and each thread executes a lot of operations.
   The operations to be executed are randomly chosen, and with randomly chosen parameters.
3. The main thread waits for all other threads to end and, then, it checks that the invariants are obeyed.
4. The operations are synchronized in order to operate correctly.

+ The rules (which mutex what invariants it protects):
    - each BankAccount object has its own mutex Lock, that locks the
      balance for that account (together with the file log write), when an operation modifies the balance variable of that account.
    - there is also a mutex for the global operation_id variable, so that it can only be modified by one thread at a time

Testing done on:
- hardware platform:
        Processor Intel(R) Core(TM) i7-8750H CPU @ 2.20GHz, 2208 Mhz, 6 Core(s), 12 Logical Processor(s)
        Installed Physical Memory (RAM)	16.0 GB DDR4
        SSD 512 GB
- data: 5 BankAccount objects

Lock granularity changes:
- first approach: a single mutex lock for both account balance and log write
- second approach (more granularity): different mutex locks for account balance and log write

+ In order to assess the performance issues, I used 5, 10, 100 and 1000 threads, with a minimum of total 500 operations
    - 5 threads: 503 operations in 220.98 s
                 504 operations in 221.51 s with more lock granularity
    - 10 threads: 508 operations in 112.57 s
                  509 operations in 112.05 s with more lock granularity
    - 100 threads: 592 operations in 23.52 s
                   599 operations in 22.88 s with more lock granularity
                   1111 operations in 46.14 s
    - 1000 threads: 1100 operations in 12.30 s
                    1010 operations in 3.28 s with more lock granularity
                    500 operations in 2.39 s


