class computation:
    def __init__(self):
        pass

    def factorial(self, n):
        if self.n==0 or self.n==1 :
            return 1
        elif self.n<0:
            return "Invalid Number"
        else:
            temp=1
            for i in range(1, self.n + 1):
                temp = temp*i
            return temp
        
    def naturalSum(self, n):
        temp = (self.n)*(self.n + 1)/2
        return temp
    
    def testPrime(self, n):
        prime = True
        for i in range(0, int((self.n)/2) ):
            if (self.n)%i == 0:
                prime = False
            else:
                pass
        return prime
    
    


