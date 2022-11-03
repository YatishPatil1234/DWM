
def table(s,r):#cal count of selected tuples with yes and no
 l1=[]
 c=-1
 for x in r:
  c +=1
  if x==s:
   l1.append(st[c])
 pj = l1.count("yes")
 nj = l1.count("no")
 print(s,"for yes: ",pj,s,"for no : ",nj)
 return pj,nj
color=['red','red','red','yellow','yellow','yellow','yellow','yellow','red','red']
typ =['sports','sports','sports','sports','sports','SUV','SUV','SUV','SUV','sports',]
origin=['Domestic','Domestic','Domestic','Domestic','Imported','Imported','Imported','Domestic','Imported','Imported']
st=['yes','no','yes','no','yes','no','yes','no','no','yes']
ty=st.count('yes')#no of yes tuples
tn=st.count('no')#no of no tuples
py=ty/len(st) #p(yes/total no of tuples)
pn=tn/len(st) #p(no/total no of tuples)
print('yes/total no of tuples :',py,'| no/total no of tuples :',pn)
y,n=table("red",color) # X = color:red | type: SUV | origin :domestic
y1,n1=table('SUV',typ)
y2,n2= table("Domestic",origin)
pyx = (y*y1*y2*py)/(ty*ty*ty) #p(X/yes)
pnx = (n*n1*n2*pn)/(tn*tn*tn)#p(X/no)
print('for the tuple X = (color=red , type =SUV, origin = Domestic)')
print('p(x/yes) = ',pyx,' p(x/no) = ',pnx)
if pyx > pnx:
 print("yes has highest probability")
else:
 print("no has highest probability")
