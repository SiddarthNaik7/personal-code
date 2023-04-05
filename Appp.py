

#AP calculator 
print("Welcome to AP calculator")
print ("By:-Siddarth Naik (ig: itz_siddarthnaik)")
st = input("Press 'ENTER'' to continue")

print(" ")


val= int(input("Select what to find\n '0' for an\n '1' for n\n '2' for a \n '3' for d\n"))

if val == 0:
    print 
    a= float(input("Enter a\n"))
    n= int(input("Enter n\n"))
    d= float(input("Enter d\n"))
    an= a+(n-1)*d
    print("The calculated value of an is =",an)

elif val == 1:
     a= float(input("Enter a\n"))
     d= float(input("Enter d\n"))
     an= float(input("Enter an\n"))
     n= an-a
     n=n/d
     n=n+1
     print("The calculated value of n is = ",    n)


elif val == 2:
    d= float(input("Enter d\n"))
    an= float(input("Enter an\n"))
    n= int(input("Enter n\n"))
    a = n-1
    a=a*d
    a=an-a
    print("The calculated value of a is =",a)


elif val == 3:
    a= float(input("Enter a\n"))
    n= int(input("Enter n\n"))
    an= float(input("Enter an\n"))
    n=n-1
    d=an-a
    d=d/n
    
    print("The calculated value of d is =",d)

