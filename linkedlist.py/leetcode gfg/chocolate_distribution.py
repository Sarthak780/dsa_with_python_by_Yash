class Solution:

    def findMinDiff(self, A,N,M):
        min_diff=0
        A.sort()     
        for i in range(0,N-M+1):
            if i==0:
                min_diff=A[i+M-1]-A[i] 
            
            else:
                if A[i+M-1]-A[i] < min_diff:
                    min_diff=A[i+M-1]-A[i]
        
        return min_diff    

if __name__ == '__main__':
    t=input("enter the testcases")
    t=int(t)
    for i in range(t):
        N=int(input("enter no of packets of chocolates"))
        A=[int(x) for x in input("enter space seperated list items").split()]
        M=int(input("enter no of students"))
    obj=Solution()

    print("min difference is",obj.findMinDiff(A,N,M))    
#in this problen you have to distribute n chocolates packets among m students each can have one with minimum difference opf chocolates for more watch gfg chocolate distribution problem 