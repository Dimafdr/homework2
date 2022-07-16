from cgitb import text
from pprint import pprint
from typing import TextIO, List, Union, Dict, Any


def dict_collector(file_path):
    with open(file_path, encoding='utf-8') as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(
                    ['ingredient_name', 'quantity', 'measure'])  # - временный словарь с ингридиетом
                ingridient = file_work.readline().strip().split(' | ')  # - вот так перемещаемся по файлу
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline()
    return menu


dict_collector('recipes.txt')


def get_shop_list_by_dishes(dishes, persons=int):
    menu = dict_collector('recipes.txt')
    print('Наше меню выглядит вот так:')
    pprint(menu)
    print()
    shopping_list = {}
    # pprint(menu.keys())
    try:
        for dish in dishes:
            for item in (menu[dish]):
                # print(item['ingredient_name'])
                # print(item['measure'])
                # print(item['quantity'])
                items_list = dict([(item['ingredient_name'],
                                    {'measure': item['measure'], 'quantity': int(item['quantity']) * persons})])
                if shopping_list.get(item['ingredient_name']):
                    # print(f' Такое {items_list} уже есть в списке. Добавил еще')
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    # print(extra_item)
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item

                else:
                    # shopping_list[item['ingredient_name']]['quantity'] *= persons
                    shopping_list.update(items_list)

        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


list_of_files = ['1.txt', '2.txt', '3.txt']

print()
print('Задание №3')

def documents_reader(list_of_files) -> dict:
  content = {}
  name_f = {}
  for values in list_of_files:
    with open(values) as file:
      list_of_sting = []
      for line in file:
        list_of_sting.append(line.strip())
    name_f[len(list_of_sting)] = values
    content[len(list_of_sting)] = list_of_sting
  return [content, name_f]

new_file = '123.txt'
list_d = documents_reader(list_of_files)

def documents_writer(new_file, list_d):
    sort_content = {}
    content = list_d[0]
    name_f = list_d[1]
    with open(new_file, "w+") as file:
        sorted_keys = sorted(content, key=content.get)
        sorted_keys.reverse()
        for values in sorted_keys:
            sort_content[values] = content[values]
        for keys, items in sort_content.items():
            for key_name, value_name in name_f.items():
                if key_name == keys:
                    file.write(f'Название файла: {value_name} \n')
            file.write(f'Количество строк: {str(keys)} \n')
            for sttri in items:
                file.write(f'{sttri} \n')
            file.write('\n')
print(documents_writer(new_file, list_d))