grades = [4, 5, 3, 5, 4, 2, 5]

min_grade = grades[0]
max_grade = grades[0]
total_sum = 0
count = 0

for g in grades:
  if g < min_grade:
    min_grade = g
  if g > max_grade:
    max_grade = g
  total_sum += g
  count += 1

average_grade = total_sum / count

print(f"Минимальная оценка: {min_grade}")
print(f"Максимальная оценка: {max_grade}")
print(f"Средний балл: {average_grade}")