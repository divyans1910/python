#Array Question 3 - Duplicates
n = int(input("Enter number of elements: "))
lst = []

#Getting array elements
for i in range(0,n):
    ip = int(input(f"Element {i}: "))
    lst.append(ip)

dup = set()

for i in range(0,n):
    if lst[i] not in dup:
        dup.add(lst[i])
    else:
        print(f"The repeated element is {lst[i]}")
        

