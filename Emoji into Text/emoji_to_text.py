import demoji
#remove emojis from the text
print("To remove emojis")
text = input("Enter any text with emojis here: ")
a1 = demoji.replace(text,"")
print(a1)

# Replace emojis with descriptive text
print("To replace emojis with description")
text1 = input("Enter text with emojis: ")
s2 = demoji.replace_with_desc(text1)
print(s2)

print("Find emojis and their description")
text2 = input("Enter text here with emojis: ")
s3 = demoji.findall(text2)
print(s3)

