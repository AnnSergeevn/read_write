import os
import time
from pprint import pprint


def read_path_files():
    path1 = '1.txt'
    path2 = '2.txt'
    path3 = '3.txt'
    outout_file = "rewrite_file.txt"
    file_path_1 = os.path.join(os.getcwd(), '1.txt')  # печатается абсолютный путь до файла
    file_path_2 = os.path.join(os.getcwd(), '2.txt')  # печатается абсолютный путь до файла
    file_path_3 = os.path.join(os.getcwd(), '3.txt')  # печатается абсолютный путь до файла

    with open(file_path_1, 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
    with open(file_path_2, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
    with open(file_path_3, 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
    with open(outout_file, 'w', encoding='utf-8') as f_total:
        if len(file1) < len(file2) and len(file1) < len(file3):
            f_total.write(path1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
            f_total.write('\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
            f_total.write(path2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
            f_total.write('\n')
        else:
            f_total.write(path3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)
            f_total.write('\n')
        if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
            f_total.write(path1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
            f_total.write('\n')
        elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
            f_total.write(path2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
            f_total.write('\n')
        else:
            f_total.write(path3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)
            f_total.write('\n')
        if len(file1) > len(file2) and len(file1) > len(file3):
            f_total.write(path1 + '\n')
            f_total.write(str(len(file1)) + '\n')
            f_total.writelines(file1)
        elif len(file2) > len(file1) and len(file2) > len(file3):
            f_total.write(path2 + '\n')
            f_total.write(str(len(file2)) + '\n')
            f_total.writelines(file2)
        else:
            f_total.write(path3 + '\n')
            f_total.write(str(len(file3)) + '\n')
            f_total.writelines(file3)


if __name__ == '__main__':
    read_path_files()
    file_path = os.path.join(os.getcwd(), 'rewrite_file.txt')
    print(file_path)
    