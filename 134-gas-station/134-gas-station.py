class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = curr_gas = i = 0
        for j in range(len(gas)):
            if curr_gas < 0:
                i, curr_gas = j, 0
            total_gas += gas[j] - cost[j]
            curr_gas += gas[j] - cost[j]
        return i if total_gas >= 0 else -1