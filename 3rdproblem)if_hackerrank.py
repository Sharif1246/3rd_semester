def average(array):
    return f"{sum(set(array))/len(set(array)):.3f}"


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)