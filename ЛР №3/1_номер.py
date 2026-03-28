# TODO Напишите функцию для поиска индекса товара
def list_products(some_kind_of_list,some_products):
    index = None
    for products in some_kind_of_list:
        if products == some_products:
            index = some_kind_of_list.index(products)

    return index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = list_products(items_list,find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
