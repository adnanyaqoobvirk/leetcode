class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        def count(lo, hi):
            if lo >= hi:
                return 0
            
            mid = lo + (hi - lo) // 2
            
            cnt = count(lo, mid) + count(mid + 1, hi)
            
            left, right = lo, mid + 1
            for i in range(hi - lo + 1):
                if right > hi or (left <= mid and arr[left] <= arr[right]):
                    tmp[i] = arr[left]
                    left += 1
                else:
                    tmp[i] = arr[right]
                    cnt += mid - left + 1
                    right += 1
            
            for i in range(lo, hi + 1):
                arr[i] = tmp[i - lo]
            
            return cnt
        tmp = [-1] * n
        return count(0, n - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends