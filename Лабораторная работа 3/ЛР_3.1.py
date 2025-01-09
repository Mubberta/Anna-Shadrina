# TODO Напишите функцию для поиска индекса товара
def find_index(items, item_to_find):
    """
        Функция для поиска первого индекса товара в списке.
        :param items: Список товаров
        :param item_to_find: Товар, индекс которого мы ищем
        :return: Индекс товара или None, если товар не найден
        """
    try:
        return items.index(item_to_find)  # Используем метод index для поиска
    except ValueError:
        return None  # Возвращаем None, если товар не найден
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
