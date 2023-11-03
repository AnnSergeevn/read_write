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

if __name__ == '__main__':
    filename = "recipes.txt"
    cook_book = read_cookbook()
    time.sleep(1)
    pprint(cook_book, width=100)
