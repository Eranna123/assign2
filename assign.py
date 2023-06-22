a = [(2,5),(1,2),(4,4),(2,3),(2,1)]

List2 =[]
List3 =[]

for x in a:
    List2.append(x[1],)

List2.sort()
print(List2)

for y in List2:
    for q in a:
        if y == int (q[1],):
            List3.append(q)

print(List3)



