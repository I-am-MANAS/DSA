s1 = "ABCD"
s2 = "CDBA"
f = 1
n = len(s1)
for i in range(n):
    k = (s1[i:]+s1[:i])
    if (k == s2):
        print("True")
        f = 0
    else:
        i+=1
if f==1:
    print("False")