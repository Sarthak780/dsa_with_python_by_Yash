def bubble(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr            

arr=[int(x) for x in input('Enter elements of a list separated by space ').split()]
result=bubble(arr)
print("sorted array is ",result)    
##this code will run n*n doesnt matter whether the array is sorted or not


        
