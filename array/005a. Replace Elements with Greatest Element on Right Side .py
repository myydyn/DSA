from typing import List


class Solution:
    def replaceElements(self, arr):
        n = len(arr)
        rightMax = -1
        for  i in range(n-1, -1, -1): #range di nguoc tu 5,4,3,2,1,0
            newMax = max(rightMax, arr[i])
            arr[i] =rightMax
            rightMax = newMax

        return arr



if __name__ == "__main__":
    arr = [17,18,5,4,6,1]
    print(len(arr))  
    print(Solution().replaceElements(arr)) 
