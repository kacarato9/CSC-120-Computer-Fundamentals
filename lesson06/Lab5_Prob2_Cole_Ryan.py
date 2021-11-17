list1 = []
again = "y"
while again == "y":
    num = int(input("Enter an integer from 1 to 10:"))
    list1.append(num)
    again = input("Enter another integer?[y/n]")
    again = again.lower()
print("Number list:", list1)
print("Largest element:", max(list1))
print("Smallest element:", min(list1))
print("Sum of all elements:", sum(list1))
print("Length of list:", len(list1))
print("Average:", (sum(list1)/len(list1)))
list1.reverse()
print("List reversed:", list1)
list1.insert(0, list1[-1])
del list1[-1]
print("Last element moved to front:", list1)
