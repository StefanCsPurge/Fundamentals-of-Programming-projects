# Parallelizing techniques for polynomial multiplication - using MPI

Algorithm 1: regular polynomial multiplication
- 
- complexity: O(n^2)
- We have 2 polynomials of degree (n-1) each.
- Take an array of size 2n-2.
- Run 2 'for' loops; each will run through 0 to n-1.
- We assign the final product array like this: p[ i + j ] += A[ i ] * B[ j ]


Algorithm 2: Karatsuba
-
- complexity: O( n^log(n) )
- divide and conquer method for number/polynomial multiplication

MPI
-
- workload is distributed to nodes: divide the nr. of polynomial coefficients to the nr. of workers
- each worker sends its partial result to the master using MPI.send
- when the workers finish, the master builds the final result from all the received partial results 

Testing
-
- number of MPI processes set to: 4
- time measurement unit: ms

| P/Q Degree | Regular sequential | Regular MPI | Karatsuba sequential | Karatsuba MPI |
| ------ | ------------------ |-------------| -------------------- |---------------|  
| 6      |   8                | 47          |          0           | 49            |
| 25     |   6                | 52          |          1           | 125           |
| 25     |   8                | 47          |          2           | 50            |
| 99     |   5                | 116         |          7           | 167           |
| 222    |   11               | 70          |          11          | 118           |
| 500    |   31               | 90          |          28          | 147           |