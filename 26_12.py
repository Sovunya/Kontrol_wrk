#Задача 7
def delivery():
    print('Введите количество позиций:')
    order = int(input())
    print('Сумма доставки:')
    if order == 1:
        print('$10.95')
    if order > 1:
        price = (10.95 + 2.95*(order - 1))
        print('$',price)
delivery()