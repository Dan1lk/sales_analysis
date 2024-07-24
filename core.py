dct = {}
lst = []
def read_sales_data(file_path: str):
    '''Сохраняем покупки в список словарей, возвращаем этот список'''

    with open(file_path, 'r', encoding="utf-8") as file:
        for row in file.readlines():
            a = row.strip('\n').split(', ')
            dct["название"] = a[0]
            dct["количество"] = a[1]
            dct["цена"] = a[2]
            dct["дата"] = a[3]
            lst.append(dct.copy())
        return lst

print(read_sales_data('sales.txt'))
