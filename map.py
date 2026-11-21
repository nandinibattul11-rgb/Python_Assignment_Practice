from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]

Squared_nos = list(map(lambda x: x**2,numbers)) #map
Even_nos = list(filter(lambda x: x%2==0,numbers)) #filter
sum_nos = reduce(lambda x,y: x+y,numbers) #reduce

print("Squares: ",Squared_nos)
print("Even_nos: ",Even_nos)
print("Sum: ",sum_nos)