
#ALGO:
#use a queue - FIFO, list and pop it's first element always.
#insert root to the que.

def levelorder(self,root):
    q=[]
    q.append(root)
    res=[]

    while q:
        n=len(q)
        ls=[]
        #we traverse the que- till it's intial length,
        #this will give us the each node in curr level.
        for i in range(len(q)):
            node=q.pop(0)
            if node:
                ls.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if ls:
                res.append(ls)
    return res
