
nlist = [7,4,9,0,1]


def insertion_sort(arr):
    for key in range(1,len(arr)):
        if arr[key] < arr[key-1]:
            print("")
            print("List = ",arr)
            j = key 
            print("If List[i] < List[i-1] . . .")
            print(f"current List[i] = {arr[j]} , prev List[i-1] = {arr[j-1]}  , left item to check (current key index -> i) = {j} ")
            while j > 0 and arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                print("swap perform")
                j -= 1
                print(arr)
               
    
    return arr
                
sort = insertion_sort(nlist)
print(sort)