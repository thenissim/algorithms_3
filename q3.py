#~~~ This is a template for question 3  ~~~

#imports
from q1_28 import quick_sort_implementation
from q2_28 import merge_sort_implementation
import pandas as pd
import matplotlib.pyplot as plt

#load data:
d1 = pd.read_excel("data_1.xlsx",sheet_name= "data_1_1") #open each sheet in excel file
d2 = pd.read_excel("data_1.xlsx",sheet_name= "data_1_2")
d3 = pd.read_excel("data_1.xlsx",sheet_name= "data_1_3")
d4 = pd.read_excel("data_1.xlsx",sheet_name= "data_1_4")
d5 = pd.read_excel("data_1.xlsx",sheet_name= "data_1_5")
l1 = d1["sort_me_1"].values.tolist() #convert each data frame to list
l2 = d2["sort_me_2"].values.tolist()
l3 = d3["sort_me_3"].values.tolist()
l4 = d4["sort_me_4"].values.tolist()
l5 = d5["sort_me_5"].values.tolist()
lst = [l1,l2,l3,l4,l5] #list that contains lists, in each one is a sheet from the excel file
lst_strings = ['list 1','list 2','list 3','list 4','list 5'] #for use in the plot

#sort data and save results:
def comparison(lst): #a function that sorts the data using the previous built functions.
    counter_list_q = [] #this list will hold the counter values of quick sort function with the given lists
    counter_list_m = [] #this list will hold the counter values of merge sort function with the given lists
    for l in lst:
        ##quick sort:
        q = quick_sort_implementation(l)
        ##merge_sort:
        m = merge_sort_implementation(l)
        counter_list_q.append(q[1]) #above function returns a tuple of the sorted list and the counter. we need the counter.
        counter_list_m.append(m[1])
    return counter_list_q,counter_list_m 
#returns a tuple of two lists. each contains counter values of basic operations done for each sort function.

#plot figure:
counter_values = comparison(lst)
##quick sort:
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.plot(lst_strings, counter_values[0])
plt.suptitle("Quick Sort's basic operations counter")
##merge sort:
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.plot(lst_strings, counter_values[1])
plt.suptitle("Merge Sort's basic operations counter")
plt.show()
##combined plot:
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.plot(lst_strings, counter_values[0],counter_values[1])
plt.suptitle("Quick Sort (blue) in comperation to Merge sort (red)")