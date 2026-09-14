n = int(input())
list1 = list(map(int, input().split()))


    

j = int(input())
list2 = list(map(int, input().split()))



set1 = set(list1)
set2 = set(list2)

set3 = set1.union(set2)
set3 = set3.difference(set1.intersection(set2))

sorted_list = sorted(set3)
for k in sorted_list:
    print(k)

# This is the 4th problem for getting the 3rd star in hackerrank.
#  The code takes two lists of integers as input, finds the symmetric difference between them,
#  sorts the result, and prints each element on a new line.    