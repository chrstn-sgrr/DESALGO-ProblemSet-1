'''
Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element A[0].
Then find the second smallest element of A and exchange it with A[1]. Continue in this manner for the first n = 1 elements of A.

a.) The algorithm described is known as selection sort. 
b.) Use a loop invariant to check that the algorithm is correct, and make sure that the loop invariant fulfills the 3 necessary properties.
'''

def selection_sort(list):
    
    for i in range(len(list)): # Traverse through all list elements (Outer Loop)
        min_index = i # Find the minimum element in remaining unsorted list
        for j in range(i+1, len(list)): # (Inner Loop)
            if list[j] < list[min_index]:
                min_index = j
        
        list[i], list[min_index] = list[min_index], list[i] # Swap the found minimum element with the first element

#numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
numbers = [9, 2, 5, 4, 3, 8, 10, 1, 7, 6]

selection_sort(numbers)
print("From a array of numbers of 1-10,")
print("This is the sorted array:", numbers)
