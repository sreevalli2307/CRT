'''Time Complexity:
ex:
n = 10
print(n)
 O(1) -->Constant time
 O(n) --> single loop
O(n^2) --> Two loops
O(logn) -->Binary loops
O(n log n)--> linera arthimetic
O(2^n) -->Recursion

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i 
    return -1 
print(linear_search([10,20,30,58,46],10))
print(linear_search([10,20,30,58,46],46))
print(linear_search([10,20,30,58,46],30))
'''