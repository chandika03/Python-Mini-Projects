# Use map() to convert Celsius → Fahrenheit.
cel = input("Enter the temperature in celcius: ")
cel_list = list(map(float, cel.split()))
fah = list(map(lambda x: (x*9/5)+32,cel_list))
print(list(fah))

# Use filter() to get numbers divisible by 3.
nums = input("Enter list of numbers: ")
nums_list = list(map(int,nums.split()))
div3 = filter(lambda x:x%3==0,nums_list)
print(f"Number divisible by 3 are: {list(div3)}")

# Use lambda to sort this list by second element:
my_list = [(1,5),(2,3),(4,1),(3,8)]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)

# Return top 3 scores from a list.
def top_scores(scores):
    return sorted(scores, reverse=True)[:3]
scores = [50, 85, 90, 70, 95, 60]
print(top_scores(scores))