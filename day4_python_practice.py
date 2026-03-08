#even squares
numbers = range(1,20)
result = [x**2 for x in numbers if x%2==0]
print(result)

#Word Length Dictionary
words = ["data","science","python","model"]
word_length = {i: len(i) for i in words}
print(word_length)

#Flatten Matrix
matrix = [[1,2],[3,4],[5,6]]
flat = [num for row in matrix for num in row]
print(flat)

#Filter Dictionary
scores = {"Alex":85,"Sam":92,"John":70,"Emma":95}
fil = {name: score for name, score in scores.items() if score>80}
print(fil)