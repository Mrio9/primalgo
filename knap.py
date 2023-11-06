class item:
    
    def __init__(self,wt,val,ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.ratio = val/wt
        
    def __it__(self,other):
        return self.ratio < other.ratio
    
    def knapsack(wt,val,cap):
        itemval = [item(wt[i],val[i],i) for i in range(len(wt))]
        
        itemval.sort(key = lambda x:x.ratio,reverse = True)
        total = 0.0
        
        for i in itemval:
            curwt = i.wt
            curval = i.val
            if cap - curwt >= 0:
                cap -= curwt
                total += curval
            else:
                frac = cap/curwt
                total += curval*frac
                cap = int(cap - curwt*frac)
                break
        return total

arr1 = [10,40,20,30]
arr2 = [60,40,100,120]
capa = 50
ans = item.knapsack(arr1,arr2,capa)
print(ans)
