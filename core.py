import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

lst = []
dct = {}
dct2 = {}
dct3 = {}
def read_sales_data(file_path: str):
    '''Сохраняем покупки в список словарей, возвращаем этот список продаж.'''

    with open(file_path, 'r', encoding="utf-8") as file:
        for row in file.readlines():
            a = row.strip('\n').split(', ')
            dct["название"] = a[0]
            dct["количество"] = a[1]
            dct["цена"] = a[2]
            dct["дата"] = a[3]
            lst.append(dct.copy())
        return lst

def total_sales_per_product(sales_data):
    ''' Принимает список продаж и возвращает словарь, где ключ - название продукта,
    а значение - общая сумма продаж этого продукта.'''
    for row in sales_data:
        try:
            dct2[row['название']] += int(row['количество']) * int(row['цена'])
        except KeyError:
            dct2[row['название']] = int(row['количество']) * int(row['цена'])
    return dct2

def sales_over_time(sales_data):
    '''Считаем общую сумму продаж за определенную дату.'''

    for row in sales_data:
        try:
            dct3[row['дата']] += int(row['количество']) * int(row['цена'])
        except KeyError:
            dct3[row['дата']] = int(row['количество']) * int(row['цена'])
    return dct3

def max_profit(dct2):
    '''Какой продукт принес наибольшую выручку'''
    for key, value in dct2.items():
        if value == max(dct2.values()):
            return key

def max_sum_sales(dct3):
    '''Какого числа наибольшая сумма продаж'''
    for key, value in dct3.items():
        if value == max(dct3.values()):
            return key

def paint_chart(dct2):
    '''Построение графиков'''
    fig, axs = plt.subplots(1, 2)
    fig.set_figheight(7)
    fig.set_figwidth(16)

    #сумма продаж по каждому продукту
    x = [i for i in dct2.keys()]
    y = [i for i in dct2.values()]
    axs[0].bar(x, y, width=0.4)
    axs[0].set_title('Сумма продаж по продукту')

    #сумма продаж по дням
    x = [i for i in dct3.keys()]
    y = [i for i in dct3.values()]
    axs[1].bar(x, y, width=0.4)
    axs[1].set_title('Сумма продаж по дням')

    plt.show()

read_sales_data('sales.txt')
total_sales_per_product(lst)
sales_over_time(lst)
paint_chart(dct2)

print(f'Наибольшую выручку принесли: {max_profit(dct2)}.')
print(f'Наибольшая сумма продаж {max_sum_sales(dct3)} числа.')