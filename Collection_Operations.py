# This is the first lab of slide 2

list1 = [98,98,97,67,57,87,96,100,89,85]
max = max(list1)
min = min(list1)

sum = 0
for i in range(len(list1)):
    sum += list1[i]
avg = sum / len(list1)

list2 = [i for i in list1 if i >= 60]

set1 = set(list1)

dict1 = {
    "01":"Ahmad",
    "02":"Ali",
    "03":"Hassan",
    "04":"Mohammed"

}
# This problem is from the end of the slide 2 and lab 1