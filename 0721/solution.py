class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        fa = [i for i in range(len(accounts))]
        emailDict = dict()
        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                x = self.getFather(i, fa)
                y = emailDict.get(accounts[i][j], -1)
                if y == -1:
                    emailDict[accounts[i][j]] = x
                else:
                    fa[x] = self.getFather(y, fa)
        records = dict()
        for i in range(len(accounts)):
            fa[i] = self.getFather(i, fa)
            if fa[i] in records:
                account = records[fa[i]]
                if not account:
                    continue
                name = account[0]
                s = set([account[j] for j in range(1, len(account))])
                for j in range(1, len(accounts[i])):
                    s.add(accounts[i][j])
                records[fa[i]] = self.createNewGroup(name, s)
            else:
                s = set([accounts[i][j] for j in range(1, len(accounts[i]))])
                records[fa[i]] = self.createNewGroup(accounts[i][0], s)
        for account in records.values():
            cur = [account[i] for i in range(1, len(account))]
            res.append([account[0]] + sorted(cur))
        return res
    
    def getFather(self, u, fa):
        if u == fa[u]:
            return u
        fa[u] = self.getFather(fa[u], fa)
        return fa[u]
    
    def createNewGroup(self, name, emailList):
        ans = [name]
        for email in emailList:
            ans.append(email)
        return ans
