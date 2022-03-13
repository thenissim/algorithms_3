# ~~~ This is a template for question 1  ~~~

#implementation of quick sort

#this function gets a list and uses quick sort
def quick_sort_implementation(lst):
    
    number_of_basic_operations=quick_sort(lst,0,len(lst)-1) #input: list, first and last index of list.
    sorted_array = lst #this is the given list after it was sorted.
    
    return sorted_array, number_of_basic_operations+2 #+2: in this function we assigned 2 more variables in addition to the basic operations done until now.
    
#NOTE: we did not took the assignment of the variable 'counter' as a basic operation since it makes no difference in sorting the array.    

def quick_sort(lst,l,r,counter=0): #default assignment of 'counter' for the first calling of the function.

    if l<r:
        
        counter+=1 #assignment of q in next line
        q,counter = partition(lst,l,r,counter)
        counter=quick_sort(lst,l,q-1,counter)
        counter=quick_sort(lst,q+1,r,counter) #assignment of the final value of counter.
        
    return counter
    

def partition(lst,l,r,counter):

    pivot= lst[l]
    i = l
    j= r
    done = False
    counter+=4 #4 assignments in first lines of function.
    while done == False:
        while lst[j] > pivot:
            j-=1
            counter+=1 #arithmetic operation
        while lst[i] < pivot:
            i+=1
            counter+=1 #arithmetic operation
        if lst[i]==lst[j]: #special case
            i+=1
            counter+=1
        if i<j:
            lst[i],lst[j] = lst[j],lst[i]
            counter+=2 #2 assignments were made in the switch.
        else:
            counter+=1 #assignment of 'done' to a defferent boolean value in next line.
            done = True
    return j,counter #besides j, returns the operations counted in this function to quick_sort function.
    



    
