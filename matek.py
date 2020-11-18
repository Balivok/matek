
#A halmaz (csak a számokat írd át!)(Csak szám)
a = {1,5,2,9}
#B halmaz (csak a számokat írd át!)(Csak szám)
b = {1,6,8,4}

#------------------------------------------------------------
#ide ne nyúlj mert akkor vége az egésznek...
k = a - b
print("A\B =")
print(k)

print()

i = b - a
print("B\A =")
print(i)

print("")

l = a | b
print("AuB =")
print(l)

print("")

print("A(felül behúzva) =")
print(i)

print("")

print("B(felül behúzva) =")
print(k)


print("")
print("AnB =")
def get_proper_element(b, a):
    return set(b) & set(a)


result = get_proper_element(b, a)
for item in result:
    print("{",item,"}")

print("")
