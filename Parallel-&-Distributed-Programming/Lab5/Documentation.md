# Parallelizing techniques for polynomial multiplication

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

Testing
-
- number of threads set to: 4
- time measurement unit: ms

| P/Q Degree | Regular sequential | Regular threaded | Karatsuba sequential | Karatsuba threaded |
| ------ | ------------------ | -----------------| -------------------- | ------------------ |  
| 6      |   8                |     5            |          0           |          5         |
| 25     |   6                |     5            |          1           |  47 (no depth ctrl)|
| 25     |   8                |     4            |          2           |  20 (depth control)|
| 99     |   5                |     6            |          7           |          22        |
| 222    |   11               |     9            |          11          |          22        |
| 500    |   31               |     45           |          28          |          47        |