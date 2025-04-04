from string import ascii_letters as A,punctuation as B
from random import choice as C
from collections import Counter as D

S=A+B;m=input("Encrypted message: ").split(", ")
for i in set(m):m=[(r:=C([c for c in S if c not in m]))if x==i else x for x in m]
c="".join(m);print(f"\nCompacted:\n{c}\n")

f=" etaoinshrdlcumwfgypbvkjxqz"
o=[c for c,_ in D(c).most_common()]
t="".join({c:f[i]for i,c in enumerate(o)}.get(c,c)for c in c)
print(f"Filtered: {t}\n")

while(u:=input("Swap ('done' to end): "))!="done":t=t.replace(u,input("With: "));print(f"\nNow:\n{t}")
print(f"\nFinal:\n{t}\n")