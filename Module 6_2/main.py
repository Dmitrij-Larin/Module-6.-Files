import json
import os
import re

from utils import get_user_level, base_program, get_result

with open("questions.json", "r", encoding='utf-8') as file:
    json_content = file.read()
words_list = json.loads(json_content)

user_name = input("Введите имя: ").capitalize()
while not re.match(r'^[a-zA-Zа-яА-ЯёЁ]+$', user_name):
    name = input("Содержит неподходящие символы! Введите заново: ")
else:
    print("Имя принято")

user_lvl = input("Выберите уровень сложности:\nлёгкий, средний, сложный.\n").strip().lower()

test_words = get_user_level(user_lvl)

test_answers = base_program(test_words)

result = get_result(test_answers, words_list[1]["levels"])

print(f"\nВаш ранг:\n{result}")

json_str = json.dumps(test_answers, ensure_ascii=False, indent=2)
with open(f'{user_name}.json', 'w', encoding="utf-8") as json_file:
    json_file.write(json_str)
os.replace(f"{user_name}.json", f"User_rating/{user_name}.json")
