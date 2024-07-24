dct = {}
lst = []
dct2 = {}
def read_sales_data(file_path: str):
    '''Сохраняем покупки в список словарей, возвращаем этот список продаж'''

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
    """ Принимает список продаж и возвращает словарь, где ключ - название продукта,
    а значение - общая сумма продаж этого продукта."""
    for row in sales_data:
        try:
            dct2[row['название']] += int(row['количество']) * int(row['цена'])
        except KeyError:
            dct2[row['название']] = int(row['количество']) * int(row['цена'])
    return dct2
read_sales_data('sales.txt')
total_sales_per_product(lst)
