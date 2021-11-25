# Methods 1
"""l1 = [1,2,3,3,3,4,5,6,7,8,3,3,5,3,3,3,3,56,7]
l2 = []
for i in l1:
    #print(i)
    if i not in [3]:
        l2.append(i)
print(l2)"""


# Methods 2
"""l1 = [1,2,3,3,4,5,6,7,3,3,3,3,3,28]
l2 = []
s = [3]
for i in l1:
    if i not in l2:
        l2.append(i)
c = list(set(l2)-set(s))
print(c)"""
