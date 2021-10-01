# user-defined function for sorting the list 
# it has List as parameter
def selectionSort(List):
    #n is the length of the list
    n=len(List)

    #if list is empty
    if n==0:
        return(List)

    #if list is not empty
    for i in range(n-1):
        #we are finding minimum of the sublist from List[i] to end of the List
        minimum_sublist = min(List[i:])
        #above line of code we found the minimun of sublist, now we are getting its index
        index_minimum = List.index(minimum_sublist)
        #swapping of List[i] with List[index_minimum]
        List[i], List[index_minimum] = List[index_minimum], List[i]
    
    #returning the sorted list
    return(List)



listA = [6,4,2,1,5]
print("Initial List:", listA)

# Selection sort function is called with listA passed as argument,
# the call returns the sortedlist and it is assigned back to listA
listA = selectionSort(listA)
print("Sorted List:", listA)


'''
Output:-

Initial List: [6, 4, 2, 1, 5]
Sorted List: [1, 2, 4, 5, 6]
'''