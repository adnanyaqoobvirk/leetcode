class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods, tables, counts = set(), set(), {}
        for _, table, food in orders:
            counts[(table, food)] = counts.get((table, food), 0) + 1
            foods.add(food)
            tables.add(int(table))
        foods = sorted(foods)
        tables = sorted(tables)
        
        ans = [['Table'] + foods]
        for table in map(str, tables):
            row = [table]
            for food in foods:
                row.append(str(counts.get((table, food), 0)))
            ans.append(row)
        return ans