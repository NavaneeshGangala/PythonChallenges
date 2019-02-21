# Enter your code here. Read input from STDIN. Print output to STDOUT

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


n = int(input())
a = list(map(int, input().rstrip().split()))

m = sum(a)/n

vals =0
for i in a:
    val = (i - m)*(i - m)
    vals+=val


sd = math.sqrt(vals/n)


print(round(sd,1))
