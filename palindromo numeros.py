def palin(num):
    if isinstance(num,int)and(num > 0):
        return palin_aux(num,num,reverse(num,0))
    else:return "Error"
def palin_aux(num,num2,reverse):
    if num==0:
        return True
    elif num%10 == (num2//(10**(reverse-1))):
        return palin_aux(num//10,num2%(10**(reverse-1)),reverse-1)
    else: return False
def reverse(num,re):
    if num == 0:
        return 0
    else: return(re+1)+reverse(num//10,re)
