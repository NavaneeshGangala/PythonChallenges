# Enter your code here. Read input from STDIN. Print output to STDOUT
from operator import mul # import mul operator

n = int(input())
a = list(map(float, input().rstrip().split()))
b = list(map(float, input().rstrip().split()))
c=[]

c = map(mul,a,b)
val=sum(c)/sum(b)

print(round(val,1))
