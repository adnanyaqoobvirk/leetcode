class Solution:
def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
for i in range(len(gas)):
curr_gas = 0
for j in range(i, len(gas)):
curr_gas += gas[j]
if cost[j] > curr_gas:
break
curr_gas -= cost[j]
else:
for j in range(i):
curr_gas += gas[j]
if cost[j] > curr_gas:
break
curr_gas -= cost[j]
else:
return i
return -1