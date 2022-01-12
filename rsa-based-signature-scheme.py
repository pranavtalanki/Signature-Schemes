import math


p=int(input("Enter p : "))
q=int(input("Enter q : "))
w=int(input("Enter w : "))

n=p*q
print("n = p*q = ",p,"*",q,"=",n)
phi=(p-1)*(q-1)
print("phi = (p-1)(q-1) = (",p,"-1)(",q,"-1)=",phi)
e=int(input("Enter e : "))

def decmod(f,n):
    for d in range(1,10000):
        k=pow(f*d,1,n)
        print(f,"*",d,"mod",n,"=",k)
        if(k==1):
            break
    return d
d=decmod(e,phi)
#d=pow(e,-1,phi)
print("d=(e^-1)mod phi(n) = ",e,"^-1 mod",phi,"=",d)
print("public key : (",e,",",n,") Private key : (",d,",",n,")")
sigma=pow(w,d,n)
print("σ=w^d modn = ",w,"^",d,"mod",n,"=",sigma)
print("send the signature,sign(w,σ) = sign(",w,",",sigma,")")
print("verification : ")
print("---------------")
w=pow(sigma,d,n)
print("w=σ^d modn = ",sigma,"^",d,"mod",n,"=",w)
