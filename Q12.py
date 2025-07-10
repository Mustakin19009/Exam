word = input("Enter a word: ")
result = ''.join(c.lower() 
if i % 2 == 0 
else c.upper() 
for i, c in enumerate(word))
print(result)