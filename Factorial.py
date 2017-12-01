import math

var1=input('Insert numbers here separated by a comma. ')

#Separates the input into two different intengers
def fracdiv(var1):
    var2=[]
    if ',' in var1:
        var2=var1.split(',')
    else:
        var1=input('Wrong input. Try Again.')
        var2=fracdiv(var1)
    return var2

exe=fracdiv(var1)

#Compares the two numbers to see if the second divides the factorial of the first and then outputs the conclusion.
if math.factorial(int(exe[0]))%int(exe[1])==0:
    print(exe[1],"divides",exe[0]+'!')
else:
    print(exe[1],"does not divide",exe[0]+'!')

