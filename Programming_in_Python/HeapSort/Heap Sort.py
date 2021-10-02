""" 
Sample Input: 
    A = [ 11, 5, 9, 21, 4, 76, 10]
Sample Output: 
    Sorted Array is: 
    4
    5
    9
    10
    11
    21
    76
 """
  
# To heapify subtree rooted at index i.
def heapify(A, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left child = 2*i + 1
    r = 2 * i + 2     # right child = 2*i + 2
  
    # Check if left child of root exists and is greater than root
    if l < n and A[i] < A[l]:
        largest = l
  
    # Check if right child of root exists and is greater than root
    if r < n and A[largest] < A[r]:
        largest = r
  
    if largest != i:
        A[i],A[largest] = A[largest],A[i]  # swap
  
        heapify(A, n, largest)
  
  
# Function to sort the array
def HeapSort(A):
    n = len(A)
  
    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, n, i)
  
    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]  # swap
        heapify(A, i, 0)
  

A = [ 11, 5, 9, 21, 4, 76, 10]
HeapSort(A)
n = len(A)
print ("Sorted Array is: ")
for i in range(n):
    print ("%d" %A[i])