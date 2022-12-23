def intarray(arr, n):
    # Sort the array
    arr.sort()
    #print(arr)
    # Check for first element
    if arr[0] == arr[1]:
        #print("output=",arr[0], end = " ")  
        arro.append(arr[0])
        
    # Check for all the elements
    # if it is different its
    # adjacent elements
    for i in range(1, n -1 ):
        if (arr[i] == arr[i + 1] and arr[i] != arr[i+2] and arr[i] != arr[i-1] ):
            #print( arr[i], end = " ") 
            arro.append(arr[i])
            
    # Check for the last element
    if arr[n - 2] == arr[n - 1]:
        #print(arr[n - 1], end = " ") 
        arro.append(arr[n - 1])
    
#Driver code
if __name__ == "__main__":
    arro=[]
    arr=[10, 12, 10, 11, 13, 17, 16, 15, 11]
    arr1=[7, 3, 8, 6, 4, 6, 7, 8, 9, 8, 7] 
    data=arr
    data1=arr1
    print("\n data=",data)
    n = len(arr)
    intarray(arr, n)            
    print("\n output=",arro)
    print("\n data=",data1)
    n1 = len(arr1)
    arro=[]
    intarray(arr1,n1)
    print("\n output=",arro)
    