class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        users = defaultdict(list)
        for user, *emails in accounts:
            groups = [set(emails)]
            merged = groups[0]
            for i, s in enumerate(users[user]):
                if s & merged:
                    merged |= s
                else:
                    groups.append(s)
            users[user] = groups
        
        ans = []
        for user, groups in users.items():
            for group in groups:
                ans.append([user] + sorted(group))
        return ans