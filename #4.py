'''
Consider sorting n numbers stored in array A by first finding the smallest element of A and exchanging it with the element A[0].
Then find the second smallest element of A and exchange it with A[1]. Continue in this manner for the first n = 1 elements of A.

a.) The algorithm described is known as selection sort. 
b.) Use a loop invariant to check that the algorithm is correct, and make sure that the loop invariant fulfills the 3 necessary properties.
'''

def selection_sort(list):
    # Traverse through all list elements
    for i in range(len(list)):
        # Find the minimum element in remaining unsorted list
        min_idx = i
        for j in range(i+1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        list[i], list[min_idx] = list[min_idx], list[i]

# Example usage
numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
selection_sort(numbers)
print("Sorted array:", numbers)
