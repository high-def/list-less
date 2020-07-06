list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90]

x = input("Enter a number: ")


counter = 0
for i in list:
  if int(x) > i:
    counter += 1
print(counter)
  