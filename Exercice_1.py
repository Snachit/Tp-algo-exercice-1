n=int(input("Entrer votre nombre:"))
for i in range(2,n+1,1):
    c=0
    for j in range(1,i+1,1):
       if  i%j==0 :
            c+=1
    if (c==2):
        print("les nombre premier inferieure a",n,"sont:",i)
if n==0:
    print("sasire un nombre non nul")