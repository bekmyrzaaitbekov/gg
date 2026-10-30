score = int(input("Введите количество баллов от 0 до 100: "))

if 90 <= score <= 100:
  print("Оценка: 5")
elif 75 <= score <= 89:
  print("Оценка: 4")
elif 60 <= score <= 74:
  print("Оценка: 3")
elif 0 <= score <= 59:
  print("Оценка: 2")
else:
  print("Ошибка ввода")
  