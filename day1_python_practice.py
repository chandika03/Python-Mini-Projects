#Function that returns mean of a list
def mean(x):
    if len(x) == 0:
        return 0
    return sum(x)/len(x)
print(mean([1,2,500]))

#Function that returns median of a list
def median(x):
    sorted_list = sorted(x)
    n = len(sorted_list)
    if n == 0:
        raise ValueError("Cannot have empty list")
    if n%2 == 1:
        median = sorted_list[n//2]
    else:
        mid1 = sorted_list[n//2 - 1]
        mid2 = sorted_list[n//2]
        median = (mid1 + mid2)/2
    return median
print(median([5,1,8,6]))

#List comprehension to extract even numbers from 1–50
y = [y for y in range(1,51) if y%2 ==0]
print(y)

#Dictionary comprehension for squares {1:1, 2:4 ...}
squares = {x:x**2 for x in range(10)}
print(squares)

#Function that returns min, max, mean
def MinMaxMean(x):
    low = min(x)
    high = max(x)
    means = mean(x)
    result = print(f"Minimum is {low}, maximum is {high} and mean is {means}")
    return result
MinMaxMean([5,1,4,2,7,6,3])