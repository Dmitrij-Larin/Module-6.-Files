import os

# Укажем в консоли абсолютный путь к файлу test_file_1.txt
# my_abspath = os.path.abspath(r'.\data_path_1\test_file_1.txt')
# print(my_abspath)
# print()

# Выведем содержимое папки task_6_2_1
path_learning = r"C:\Users\dmitr\OneDrive\Documentos\Обучение на Python\Module 6. Homework\Module 6_1\task_6_2_1"
for path, dirnames, filenames in os.walk(path_learning):
    print(f"path - {path}")
    print(f"dirnames - {dirnames}")
    print(f"filenames - {filenames}")



