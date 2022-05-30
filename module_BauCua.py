class BauCua:
    def __init__(self, dices):    #khoi tao gia tri ban dau, truyen tham so mang dices
        self.x=[0]*15
        self.Dices=dices
        self.somat=len(self.Dices)
        self.n=self.somat
        self.tonghop=[]
        for i in range(self.somat+1): self.tonghop.append([0]*6);
        self.s=0
        self.k=0

    def solve(self, col):   #ham de xu ly tung to hop
        global s
        check=[True]*15
        ans=1
        for i in range(1, self.k+1):
            check[self.x[i]-1]=False
        for i in range(self.somat):
            sum=0
            for j in range(0, 6):
                if j!=col:
                    if check[i]==True:
                        sum+=self.Dices[i][j]
            if check[i]==True: ans*=sum
        for i in range(self.somat):
            if (check[i]==False):
                ans*=self.Dices[i][col]
        self.s+=ans

    def combination(self, i, col):   #ham sinh to hop index
        j=self.x[i-1]+1
        while j<=self.n-self.k+i:
            self.x[i]=j
            if self.k==0: 
                self.solve(col)
                return
            else:
                if i==self.k: self.solve(col)
                else: self.combination(i+1, col)
                j+=1

    def cal(self):   #ham tinh toan
        
        for i in range(0, self.n+1):   
            self.k=i
            for col in range(0, 6):
                self.s=0
                self.x=[0]*15
                self.combination(1, col)
                self.tonghop[i][col]=self.s
        

# bc = BauCua([[1, 2, 2, 1, 1, 3], [1, 1, 1, 1, 1, 2], [1, 3, 2, 1, 1, 2]])
# bc.cal()
# print(bc.tonghop)