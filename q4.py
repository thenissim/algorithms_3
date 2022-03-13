def bubble_sort(lst):

    counter=0
    for i in range (0, len(lst)-1):
        counter+=1 #assignment of i 
        for j in range(0,len(lst)-1-i):
            counter+=1 #assignment of j
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                counter+=2 #2 assignments were made in the switch
    return lst,counter
