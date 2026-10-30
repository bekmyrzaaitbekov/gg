n = len(arr)

for i in range(n):
  min_idx = i
  for j in range(i + 1, n):
    if arr[j] < arr[min_idx]:
      min_idx = j
  # Меняем местами
  arr[i], arr[min_idx] = arr[min_idx], arr[i]

print("По возрастанию:", arr)

arr2 = [4, 2, 5, 3, 5, 4, 3]
for i in range(n):
  max_idx = i
  for j in range(i + 1, n):
    if arr2[j] > arr2[max_idx]:
      max_idx = j
  arr2[i], arr2[max_idx] = arr2[max_idx], arr2[i]

print("По убыванию:", arr2)