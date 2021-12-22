class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        q, zero = deque(arr), False
        for i in range(len(arr)):
            if not q[0]:
                if zero:
                    q.popleft()
                    zero = False
                else:
                    zero = True
                arr[i] = 0
            else:
                arr[i] = q.popleft()