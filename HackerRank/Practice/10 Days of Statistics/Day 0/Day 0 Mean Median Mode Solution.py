# Enter your code here. Read input from STDIN. Print output to STDOUT
import pandas as pd
import statistics 
import numpy as np
n = int(input())
ar = list(map(int, input().rstrip().split()))
m = pd.Series(ar).mean()
me = pd.Series(ar).median()


unique, counts = np.unique(ar, return_counts=True)
x = pd.DataFrame(zip(unique, counts))
x.columns = ['unique', 'counts']
mo = x[x['counts'] == max(x['counts'])].unique.min()



print(m)
print(me)
print(mo)

