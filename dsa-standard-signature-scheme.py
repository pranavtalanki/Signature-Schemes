import math


p=int(input("Enter p : "))
q=int(input("Enter q : "))
h=int(input("Enter h : "))
w=int(input("Enter w : "))
x=int(input("Enter x : "))

j1=int((p-1)/q)

r=pow(h,j1,p)
print("r = h^(p-1/q)modp = ",2,"^(",p,"-1/",q,")mod",p,"=",r)
y=pow(r,x,p)
print("y=r^x modp=",r,"^",x,"mod",p,"=",y)
print("Public key =(p,q,r,x,y)=(",p,",",q,",",r,",",x,",",y,")")
print("Signature : ")
print("------------")
k=0
for i in range(2,q):
    i1=math.gcd(i,q)
    if(i1==1):
        k=i
        break

print("k=",k)
a1=pow(r,k,p)
a=pow(a1,1,q)
print("a=(r^k mod p)mod q = (",r,"^",k,"mod",p,")mod",q,"= ",a1,"mod",q,"=",a)
def decmod(e,n):
    for d in range(1,1000):
        k=pow(e*d,1,n)
        print(e,"*",d,"mod",n,"=",k)
        if(k==1):
            break
    return d
print("ki = ")
ki=decmod(k,q)
print("ki=",ki)
b1=w+x*a
b=pow(ki*b1,1,q)
print("b = k^(-1)(w+xa)modq = ",ki,"(",w,"+",x,"*",a,"mod",q,")= ",ki,"*",b1,"mod",q,"= ",b)
print("verification : ")
print("---------------")
print("z=")
z=decmod(b,q)
print("z=",z)
u1=pow(w*z,1,q)
print("u1=wz modq = ",w,"*",z,"mod",q,"=",u1)
u2=pow(a*z,1,q)
print("u2=az modq = ",a,"*",z,"mod",q,"=",u2)
e1=pow(r,u1)
e2=pow(y,u2)
e3=pow(e1*e2,1,p)
e4=pow(e3,1,q)
print("((r^u1)*(y^u2)modp)modq = (",r,"^",u1,"*",y,"^",u2,"mod",p,")mod",q,"=",e4,"= a")
print("sign has been checked and verified")