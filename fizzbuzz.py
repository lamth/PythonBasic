i = 0
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i,"fizzbuzz")
        continue
    elif i % 3 == 0:
        print(i,"fizz")
        continue
    elif i % 5 == 0:
        print(i,"buzz")
        continue
    print(i)
