"""
==============================================================================================================
[13] The sequence 𝑎1,..., 𝑎𝑛 of distinct integer numbers is given. Display all subsets with a mountain aspect.
Solve the problem using the BACKTRACKING programming method,
using an ITERATIVE and a RECURSIVE implementation for the ‘backtracking’ procedure.
==============================================================================================================
"""
def mountain(a):
    """
    Function that checks if a given sequence of integers has a mountain aspect.
    A set has a mountain aspect if the elements increase up to a point and then they decrease.
    E.g. 10, 16, 27, 18, 14, 7
    :param a: the given list of integers
    :return: True/False
    """
    n = len(a)
    if n < 3: return False
    climbLeft = 0
    climbRight = n-1
    while a[climbLeft] < a[climbLeft+1]:
        climbLeft += 1
        if climbLeft == n-1:
            return False
    while a[climbRight] < a[climbRight-1]:
        climbRight -= 1
        if climbRight == 0:
            return False
    if climbLeft != climbRight:
        return False
    return True

def IterativeBack(nums):
    if not len(nums): return
    temp = [nums[0]]
    start = 1
    while temp[0] != nums[-1]:
        if mountain(temp):
            printSol(temp)
        if start < len(nums):
            temp.append(nums[start])  # construct the next subset
            start += 1
        else:  # backtrack
            temp.pop()
            start = nums.index(temp[-1])+1
            temp[-1] = nums[start]
            start += 1

def RecursiveBack(temp, nums, start):
    if mountain(temp):
        printSol(temp)
    for i in range(start, len(nums)):
        temp.append(nums[i])
        RecursiveBack(temp, nums, i + 1)
        temp.pop()  # backtrack

def printSol(solution):
    global solIdx
    solIdx += 1
    print("{}: {}".format(solIdx, solution))


if __name__ == '__main__':
    print("Enter the numbers of your sequence. Enter any letter to end the input.")
    s = []
    while True:
        try:
            x = int(input("Insert number: "))
            if x in s:
                print("Number already in set!")
            else:
                s.append(x)
        except Exception as ex:
            ex = str(ex)
            print("Input ended.\n")
            break

    print('Iterative backtracking:')
    solIdx = 0
    IterativeBack(s)
    if not solIdx:
        print('There are no mountains!')

    print('\nRecursive backtracking:')
    solIdx = 0
    RecursiveBack([], s, 0)
    if not solIdx:
        print('There are no mountains!')
