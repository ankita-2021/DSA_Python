
#floor expression
'''def sumofproduct(n):
    summ=0 # 5, 9, 12, 16, 21
    for x in range(1,n+1): #x=1 to 5
        y=n//x #5//1,,5//2,, 5//3 ,, 5//4 ,, 5//5
        summ=summ+(x*y)  #0+1*5=5 ,,5+2*2=9,, 9+3*1=12,, 12+4*1=16,, 16+5*1= 21
    return summ #21
n = int(input()) #5
print(sumofproduct(n))'''