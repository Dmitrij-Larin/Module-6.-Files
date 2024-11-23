import os

# Укажем в консоли абсолютный путь к файлу test_file_1.txt
# my_abspath = os.path.abspath(r'.\data_path_1\test_file_1.txt')
# print(my_abspath)
# print()

# Выведем содержимое папки task_6_2_1
# path_learning = r"C:\Users\dmitr\OneDrive\Documentos\Обучение на Python\Module 6. Homework\Module 6_1\task_6_2_1"
# for path, dirnames, filenames in os.walk(path_learning):
#     print(f"path - {path}")
#     print(f"dirnames - {dirnames}")
#     print(f"filenames - {filenames}")
# print()

# Укажем абсолютный путь к файлу test_file_3.txt с помощью функции os.path.join()
disk = 'C:\\'
dir_1 = 'Users'
dir_2 = 'dmitr'
dir_3 = 'OneDrive'
dir_4 = 'Documentos'
dir_5 = 'Обучение на Python'
dir_6 = 'Module 6. Homework'
dir_7 = 'Module 6_1'
dir_8 = 'task_6_2_1'
dir_9 = 'data_path_2'
file = 'test_file_3.txt'
path_test_file_3 = os.path.join(disk, dir_1, dir_2, dir_3, dir_4, dir_5, dir_6, dir_7, dir_8, dir_9, file)
print(path_test_file_3)
print()

# Создадим папки внутри папки data_path_2
base_dir = '.'
test_dir = 'data_path_2'
new_dir_1 = r'my_new_dir_1'
new_dir_2 = r'my_new_dir_2'
path_new_dir_1 = os.path.join(base_dir, test_dir, new_dir_1)
path_new_dir_2 = os.path.join(base_dir, test_dir, new_dir_2)
os.mkdir(path_new_dir_1)
os.mkdir(path_new_dir_2)



