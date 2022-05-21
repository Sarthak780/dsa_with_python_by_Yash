def selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min]= arr[min],arr[i]        
    
    return arr

arr=[10,21,15,40,18,35,9]
result=selection_sort(arr)
print(result)

