m=int(input("Enter the mass of a body:"))
g=10
f=m*g
s=int(input("Enter the displacement due to force on the body:"))
cos=int(input("Enter the angle between the displacement and the direction of force(The angle should be 90,180 or 0):"))
cos18=-1
cos9=0
cosa=1
a=f*s*0
b=f*s*-1
c=f*s*1
w=f*s
if cos==90:
     print("The work done is:",a,"J")
elif cos==180:
    print("The work done is:",b,"J")
elif cos==0:
    print("The work done is:",c,"J")
else:
    print("ERROR")
