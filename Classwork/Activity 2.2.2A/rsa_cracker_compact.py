from string import ascii_letters as A, punctuation as B
from random import choice as C
from collections import Counter as D

S=A+B;m=input("Encrypted message: ").split(", ")
for i in set(m):
 if(v:=[c for c in S if c not in m]):m=[(r:=C(v))if x==i else x for x in m]
c="".join(m);print(f"\nCompact:\n{c}\n")
F=" etaoinshrdlcumwfgypbvkjxqz"
o=[c for c,_ in D(c).most_common()]
t="".join({c:F[i]for i,c in enumerate(o[:len(F)])}.get(c,c)for c in c)
print(f"Filtered:\n{t}\n")
while(u:=input("Swap letter ('done' to end): "))!="done":t=t.replace(u,input("With: "));print(f"\nNow:\n{t}")
print(f"\nFinal:\n{t}\n")