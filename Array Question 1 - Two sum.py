#Array Question 1 - Two sum

n = int(input("Enter number of elements in array: "))
lst = []

#Getting array elements
for i in range(0,n):
    ip = int(input(f"Element {i}: "))
    lst.append(ip)

#Getting sum required
sum = int(input("Enter sum: "))  
    
#Subracting the sum from the array element and finding if the element exists in the array    
for j in range(0,n):
    rem = sum - lst[j]
    if rem in lst and rem != lst[j]:
        ind = lst.index(rem)
        print(f"[{j},{ind}]") #printing all the possible indices

    