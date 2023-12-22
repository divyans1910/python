#Array Question 2 - Stocks
n = int(input("Enter number of days: "))
lst = []

#Getting array elements
for i in range(0,n):
    ip = int(input(f"Day {i}: "))
    lst.append(ip)

#Getting index of min value
x = min(lst)
ind = lst.index(x)

profit = []

#Finding most profit from min stock day
for i in range(ind+1, n):
    s = ind
    rem = lst[i] - lst[s]
    profit.append(rem)

if len(profit) == 0: #No profit case
    maxprofit = 0
else:
    maxprofit = max(profit) #Finding max profit


print(f"Maximum profit achieved: {maxprofit}")
    