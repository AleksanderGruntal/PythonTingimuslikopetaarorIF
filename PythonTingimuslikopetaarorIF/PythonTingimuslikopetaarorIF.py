# Ülesanne 21
from math import *
from random import *
while True:
    nimi=input("Mis on sinu nimi? ")
    if nimi.isalpha(): break
# Ülesanne 0.2
x=int()
s=0
viimane=0
pr=1
maksimaalselt=3
miinimum=0
# Ülesanne 8.2
a=1
while True:
    print(a)
    if a >= 100:
        break
    a+=1
# Ülesanne 0
while True:
    a=input("Kas sa tahad endale uue arvuti osta?: ")
    if a.upper()=="JÄH" or a.upper()=="EI": break
if a.upper()=="JÄH":
    while True:
        c=input("Kas tahad mänguarvuti või tavalist?: ")
# Ülesanne 6
n=0
print ("kolmnurga")
for e in range (11, 0, -1):
    n = n + 1
    for f in range (1, n+1):
        print("*", end = "")
    print()
print("")

# Ülesanne 6.1
for x in range(5):
    print("******")
    
# Ülesanne 6.2
for g in range (11,0, -1):
    n = n - 1
    for h in range (0, n-1):
        print("*", end = "")
    print()
print("")
# Ülesanne 6.3
for i in range(1,5):
    x=str("*"*i, end="").center(18," ")
    print(x, end="")
    print()
for i in range(1,10):
    x=str("*"*(i+2)).center(18," ")
    print(x, end="")
    print()
for i in range(1,15):
    x=str("*"*(i+4)).center(18," ")
    print(x, end="")
    print()

# Ülesanne
 