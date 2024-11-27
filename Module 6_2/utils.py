import json

with open("questions.json", "r", encoding='utf-8') as file:
    json_content = file.read()
words_list = json.loads(json_content)


def get_user_level(user_lvl):
    if user_lvl == "лёгкий":
        words = words_list[0]["questions"][0]
        print("Вы выбрали лёгкий уровень сложности")
    elif user_lvl == "средний":
        words = words_list[0]["questions"][1]
        print("Вы выбрали средний уровень сложности")
    elif user_lvl == "сложный":
        words = words_list[0]["questions"][2]
        print("Вы выбрали сложный уровень сложности")
    else:
        words = words_list[0]["questions"][0]
        print("Вам автоматически выбран лёгкий уровень сложности")

    return words


answers = {}


def base_program(words):
    for key, value in words.items():
        answer = input(f"{key}, {len(value)} букв, начинается на \"{value[0]}\"...").lower().strip()
        if answer == value:
            print(f"Верно! {key} - это {value}")
            answers.update({key: True})
        else:
            print(f"Неверно! {key} - это {value}")
            answers.update({key: False})

    return answers


def get_result(answers, levels):
    keys_True = [key for key, value in answers.items() if value == True]
    keys_False = [key for key, value in answers.items() if value == False]
    print(f"\nПравильно отвеченные слова:\n"
          f"{'\n'.join(keys_True)}")
    print()
    print(f"Неправильно отвеченные слова:\n"
          f"{'\n'.join(keys_False)}")
    count = len(keys_True)
    rank = levels.get(str(count))

    return rank
