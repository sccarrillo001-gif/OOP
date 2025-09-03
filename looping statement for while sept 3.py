#PART 1-------------------------------------------

'''
for number in range(1,20):
    if number%2 == 0:
        print (number, " is even")
    else:
        print(number, " is odd")
'''

#PART 2----------------------------------------

'''
n= int(input("write the number"))

for number in range(1,16):
    print(number, "x", n, "=", n*number)
'''
#PART 3----------------------------------------

p = int(input("write p"))
n = int(input("write n"))
R = int(input("write R"))

r= R/(n*100)
EMI = p *r * ((1+r)**n)/((1+r)**n-1)


for number in range(1,n+1):

    balance = p- EMI
    print("EMI: ", EMI)
    print("Balance: ", balance)
    print("....")
    p=balance
