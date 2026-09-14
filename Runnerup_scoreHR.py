n = int(input())
scores = list(map(int, input().split()))

sorted_scores = sorted(set(scores), reverse=True)
print(sorted_scores[1])

# This is a problem from Hackerrank called "Find the Runner-Up Score!" where you are given a list of scores and you need to find the second highest score. The code takes an integer input for the number of scores, then takes a list of scores as input, removes duplicates by converting it to a set, sorts it in descending order, and finally prints the second highest score.