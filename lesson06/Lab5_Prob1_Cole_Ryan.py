import copy

list1 = []
for i in range(5):
    score = float(input("Enter a test score:"))
    list1.append(score)
print("All scores:", list1)

list2 = copy.deepcopy(list1)
print("Students who scored below 60 get 10 extra points.")
for i in range(len(list2)):
    if list2[i] < 60:
        list2[i] = list2[i] + 10
print("All scores:", list2)
print("Students whose scores have changed:")
for i in range(len(list1)):
    if list1[i] != list2[i]:
        print("Old score:", list1[i], " New score:", list2[i])
