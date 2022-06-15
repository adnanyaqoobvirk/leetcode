class Solution:
    def average(self, salary: List[int]) -> float:
        max_salary = -inf
        min_salary = inf
        total = 0
        for s in salary:
            max_salary = max(max_salary, s)
            min_salary = min(min_salary, s)
            total += s
        total -= max_salary + min_salary
        return total / (len(salary) - 2)