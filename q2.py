# ~~~ This is a template for question 2  ~~~

#implementation of merge sort

#this function gets a list and uses merge sort

#NOTE: we chose not to count comperations as a basic operation.
def merge_sort_implementation(lst):
    
    counter = merge_sort(lst,0,len(lst)-1) #input: list, first and last index of list.
    sorted_array = lst #this is the given list after it was sorted.
    number_of_basic_operations = counter
    
    return sorted_array, number_of_basic_operations+2 #+2: two more variables were assigned.


def merge_sort(lst,first,last,counter=0): #default assignment of 'counter' for the first calling of the function.

    if first < last:

        middle = (first + last)//2
        counter+=3 #assignment plus two arithmetic operations.
        counter=merge_sort(lst,first,middle,counter)
        counter=merge_sort(lst,middle+1,last,counter) #assignment of the final 'counter' value.
        counter=merge(lst,first,middle,last,counter) 
        
    return counter


def merge(lst,first,middle,last,counter):

    L = lst[first:middle+1]
    R = lst[middle+1:last+1]
    i,j,org = 0,0,first
    counter+=5 # 5 assignments were made
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            lst[org] = L[i]
            i+=1
            counter+=2 # 2 assignments were made
        else:
            lst[org] = R[j]
            j+=1
            counter+=2 # 2 assignments were made
        org+=1
        counter+=1 #assignment
    while i < len(L):
        lst[org] = L[i]
        i+=1
        org+=1
        counter+=3 # 3 assignments were made
    while j < len(R):
        lst[org] = R[j]
        j+=1
        org+=1
        counter+=3 # 3 assignments were made

    return counter #returns operations counted in this function to merge_sort function.
