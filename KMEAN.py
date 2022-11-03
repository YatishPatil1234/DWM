 
#implementing k-mean algorithm
# k =int(input("no of cluster: "))
#enter length of list1
x = int(input("enter length : "))
dataset = [0] * x
for i in range(x):
 dataset[i]= int(input("enter dataset"))
list1 = dataset
m=list1
print("DATASET: ",m)
n= int(len(m))
# randomly selecting mean
m1 = list1[0]
m2= list1[n-1]
print("mean m1 :",m1)
print("mean m2 :",m2)
#first iteration
iteration = 1
p=[0]*x #declaring array
q=[0]*x
for i in range(n ):
 g = abs(m1-m[i])
 h = abs(m2-m[i])
 if g<h :
  p[i]=m[i]
 else:
  q[i]=m[i]
print("CLUSTER 1 p: ",p)
print("CLUSTER 2 q: ",q)
print("ITERATION NO : ",iteration)
#removing zero from clusters
q=list(filter(lambda num: num != 0, q))
p=list(filter(lambda num: num != 0, p))
print(p,q)
