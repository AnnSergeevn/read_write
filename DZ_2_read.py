import os
import time
from pprint import pprint


def read_cookbook():
    file_path = os.path.join(os.getcwd(), 'recipes.txt')  # печатается абсолютный путь до файла
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as f:    # открытие файла на чтение
        for line in f:
            dish_name = line.strip()                     #1 ая строка с названиями блюд, обрезка строки str с обоих концов
            count = int(f.readline())                    # 2ая строка количество инградиентов
            ing_list = list()
            for item in range(count):
                ingrs = {}
                ingr = f.readline().strip()
                ingrs['ingredient_name'], ingrs['quantity'], ingrs['measure'] = ingr.split('|')
                ingrs['quantity'] = int(ingrs['quantity'])
                ing_list.append(ingrs)
            f.readline().split()
            cook_book[dish_name] = ing_list
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()
    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingredient_name'] not in ingr_list:
                    meas_quan_list['measure'] = ings['measure']
                    meas_quan_list['quantity'] = ings['quantity'] * person_count
                    ingr_list[ings['ingredient_name']] = meas_quan_list
                else:
                    ingr_list[ings['ingredient_name']]['quantity'] = ingr_list[ings['ingredient_name']]['quantity'] + \
                                                                     ings['quantity'] * person_count
        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list


if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = read_cookbook()
    pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
