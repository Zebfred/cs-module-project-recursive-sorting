# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    

    # Your code here
    if start > end:
        return -1
    middle = (start + end) // 2
    if arr[middle] == target:
        return middle
    else:
        if arr[middle] > target:
            return binary_search(arr, target, start, middle - 1)
        if arr[middle] < target:
            return binary_search(arr, target, middle+1, end)
    return -1    

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass

def ago_bi_search(arr, l, h, key):
    
    if (l > h) :
        return -1;
    mid = ( l + h) // 2;
    if (arr[mid] == key) :
        return mid;
    
    #update left and right?
    if ((arr[l] == arr[mid]) and (arr[h] == arr[mid])):
        l += 1;
        h -= 1;
        
        if (arr[l] <= arr[mid] ) :
            
            #subarray sorted
            if (key >= arr[l] and key <= arr[mid]) :
                return ago_bi_search(arr, l, mid - 1, key);
            
            #does not lie in fist halve
            return ago_bi_search(arr, mid + 1, h, key);
            
    #if arr[l...mid] not sorted 
    #arr[mid to high] is sorted
    if (key >= arr[mid] and key <= arr[h]) :
        return ago_bi_search(arr, mid + 1, h , key);
    
    return ago_bi_search(arr, l, mid - 1, key);

if __name__ == "__main__" : 
            
        
         
    descending = [101, 98, 57, 49, 45, 13, -3, -17, -61];
    lenth = len(descending);
    key_d = 98;
    print(search(descending, 0,lenth - 1, key_d));        