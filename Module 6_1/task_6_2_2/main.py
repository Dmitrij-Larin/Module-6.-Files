with open("write_data.txt", "wt", encoding="utf_8") as file:
    file.write("Если б мишки были пчелами,\n")
    file.write("То они бы нипочем,\n")
    file.write("Никогда и не подумали,\n")
    file.write("Так высоко строить дом.")

with open("write_data.txt", "r", encoding="utf_8") as file:
    data = file.read()
print(data)