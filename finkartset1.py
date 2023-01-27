def longesSubstring(str1 , str2){
    ans = 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            k = 0 
            while ((i + k) < len(str1) and ( j + k ) < (str2)):
                k = k + 1
            i = max(ans , k)   
    return ans
}

# code for find the number in array to add to target
def addToTarget( arr, key):
    for i in range(arr.length):
        for j in range(arr.length):
            if(arr[i] + arr[j] == key):
                return [arr[i] , arr[j]]
