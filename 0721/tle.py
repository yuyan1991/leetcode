class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        res = []
        fa = [i for i in range(len(accounts))]
        for i in range(len(accounts)):
            for j in range(i):
                if self.isSameAccount(accounts[i], accounts[j]):
                    fa[self.getFather(j, fa)] = self.getFather(i, fa)
        
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
                records[fa[i]] = self.createNewGroup(name, sorted(s))
            else:
                s = set([accounts[i][j] for j in range(1, len(accounts[i]))])
                records[fa[i]] = self.createNewGroup(accounts[i][0], sorted(s))
        for account in records.values():
            res.append(account)
        return res
    
    def isSameAccount(self, acc1, acc2):
        for i in range(1, len(acc1)):
            for j in range(1, len(acc2)):
                if acc1[i] == acc2[j]:
                    return True
        return False
    
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

# Time Limited Exceed