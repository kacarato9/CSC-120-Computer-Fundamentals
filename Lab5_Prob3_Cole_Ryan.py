dict = {}
word = input("Enter a string:")
word = word.upper()
for i in word:
    if i not in dict and i.isalpha():
        dict[i] = word.count(i)
print("Dictionary:", dict)

search = input("Choose a letter:")
search = search.upper()
if search in dict:
    print("Frequency count of that letter:", dict[search])
    del dict[search]
    print("Dictionary after that letter removed:", dict)
else:
    print("Letter not in dictionary")
list1 = list(dict.keys())
list1.sort()
print("Letters sorted:", list1)
