import random
number = random.randrange(3, 21)
print(f'{number} - число из первой вставки' ) # Число из первого поля
def cod():
    for i in range(1, number):  # Не знаю зачем это все через функцию, ну раз изучили надо использовать :)
        for j in range(1, number):
            if i >= j :
                continue
            else:
                summa = i + j
            if number % summa == 0:
                result = int(f'{i}{j}')
                print(result, end = '')
cod()











