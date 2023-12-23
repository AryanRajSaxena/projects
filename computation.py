class computation:
    def __init__(self):
        pass

    def factorial(self, n):
        if n==0 or n==1 :
            return 1
        elif n<0:
            return "Invalid Number"
        else:
            temp=1
            for i in range(1,n + 1):
                temp = temp*i
            return temp
        
    def naturalSum(self, n):
        temp = (n)*(n + 1)/2
        return temp
    
    def testPrime(self, n):
        prime = True
        for i in range(2, int((n)/2) ):
            if (n)%i == 0:
                prime = False
            else:
                pass
        return prime
    
    


