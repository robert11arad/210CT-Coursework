number = int(input('Insert a number. '))
def Binary_Converter(nr):
    suma=1
    nrs=0
    x=1
    cod=[]
    alpha=2*4

    if nr<0:
        cod.append('-')
        nr=nr*(-1)

    while nr/x>=2:
        x=x*2
        nrs=nrs+1
        suma=suma+x

    while nr<alpha:
        cod.append('0')
        alpha=alpha/2
        if alpha==1:
            break

    for i in range(nrs+1):
        if nr>=x:
            nr=nr-x
            cod.append('1')
        else:
            cod.append('0')
        x=x/2
    return(''.join(cod))

def Binary2nd_Converter(nr):
    suma=1
    nrs=0
    x=1
    cod=[]
    if nr<-2147483647 or nr>2147483647:
        return ("Can't calculate.")
    if nr<0:
        nr=nr*(-1)

        if nr<2**16-1:
            alpha=2**15
        else:
            alpha=2**31
        while nr<alpha:
            cod.append('1')
            alpha=alpha/2
            if alpha==1:
                break
            
        nr=nr-1
        
        while nr/x>=2:
            x=x*2
            nrs=nrs+1
            suma=suma+x

        for i in range(nrs+1):
            if nr>=x:
                nr=nr-x
                cod.append('0')
            else:
                cod.append('1')
            x=x/2
            
    elif nr>=0:

        if nr<2**16-1:
            alpha=2**15
        else:
            alpha=2**31
        while nr/x>=2:
            x=x*2
            nrs=nrs+1
            suma=suma+x
        while nr<alpha:
            cod.append('0')
            alpha=alpha/2
            if alpha==1:
                break
            
        for i in range(nrs+1):
            if nr>=x:
                nr=nr-x
                cod.append('1')
            else:
                cod.append('0')
            x=x/2
            
    return(''.join(cod))

print('Number: ',number,'\nBinary: ',Binary_Converter(number),'\n2nd Form binary: ',Binary2nd_Converter(number))






