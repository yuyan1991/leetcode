class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        for account in accounts:
            flag = True
            for i in range(len(res)):
                cur = res[i]
                name = cur[0]
                s = set()
                for j in range(1, len(cur)):
                    s.add(cur[j])
                for j in range(1, len(account)):
                    if account[j] in s:
                        flag = False
                        break
                if not flag:
                    for j in range(1, len(account)):
                        s.add(account[j])
                    res[i] = [name]
                    for email in sorted(s):
                        res[i].append(email)
                    break
            if flag:
                name = account[0]
                s = set()
                for j in range(1, len(account)):
                    s.add(account[j])
                newGroup = [name]
                for email in sorted(s):
                    newGroup.append(email)
                res.append(newGroup)
        return res

# Wrong Answer
# Input:
# [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
# Output:
# [["David","David0@m.co","David1@m.co","David2@m.co"],["David","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
# Expected Output:
# [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]
