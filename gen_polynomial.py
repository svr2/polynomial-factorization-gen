import random
'''
--------------------------------------
Variable Naming Explanation
----------------------------------
in a quadratic equation ax^2 + bx + c :
aCoef = a
bCoef = b
cCoef = c

**Note**  a and b mean stand for something different in the line below
in terms of the roots/zeroes (x+a)(x+b):
rt1 = -a (since x + a = 0)
rt2 = -b (since x + b = 0)

'''

class Problem():
    #qContent is what the question will look like in string form
    qContent = '--ERROR--'

    bCoef = None
    aCoef = None
    cCoef = None

    def __init__(self):

        self.data = []

        rt1 = 1
        rt2 = 1

        while True:
            rt1 = random.randrange(-20,20)
            rt2 = random.randrange(-20,20)
            if ( rt1*rt2 != 0 ):
                break

        bCoef = -rt1 + -rt2

        coefFactors = []
        coefNumerator = rt1*rt2

        # Took the square root of numerator to reduce number of calculations and increase efficiency
        '''
        Why I did that:
        a = m x n
        if m > sqrt(a) , then n < sqrt (b)
        '''
        for i in range(1,int((abs(coefNumerator)**0.5))):
            if coefNumerator % i == 0:
                coefFactors.append(i)

        aCoef = coefNumerator/random.choice(coefFactors)
        cCoef = coefNumerator/aCoef



        self.qContent = ('Factorize:\n'+ str(aCoef)+'x^2 + '+str(bCoef)+'x + '+str(cCoef) + '\nAnswer:\n' + '(x + '+str(-rt1)+') (x + '+str(rt2)+')\n\n')


inpt = input('How many problems would you like to generate?')

for i in range (inpt):
    print Problem().qContent
