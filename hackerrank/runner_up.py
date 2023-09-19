n = int(input())
arr = list(map(int, input().split()))

arr1 = list(set(arr))
arr1.sort(reverse = True)

runner_up = arr1[1]
print(runner_up)