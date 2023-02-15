import json

with open ("quastion.json", "w") as file:
    quastion = {
        "Транспорт": {
            "100": {"quastion":"plane", "answer":"самолет", "asked":"False"},
            "200": {"quastion":"train", "answer":"поезд", "asked":"False"},
            "300": {"quastion":"boarding", "answer": "посадка", "asked": "False"},
        },
        "Животные": {
            "100": {"quastion": "dog", "answer": "собака", "asked": "False"},
            "200": {"quastion": "shark", "answer": "акула", "asked": "False"},
            "300": {"quastion": "table", "answer": "стол", "asked": "False"},
        },
        "Еда": {
            "100": {"quastion": "apple", "answer": "яблоко", "asked": "False"},
            "200": {"quastion": "tomato", "answer": "помидор", "asked": "False"},
            "300": {"quastion": "banana", "answer": "банан", "asked": "False"},
        }
    }
    file.write(json.dumps(quastion))
tru_answer_user = 0
false_qnswer_user = 0
sum_coins = 0
def show_table():
    with open ("quastion.json", "r") as file:
        title = json.loads(file.read())
        for category in title:
            print(category, end=" ")
            for point in title[category]:
                if title[category][point]["asked"] == "False":
                    print(point, end=" ")
                else:
                    print("   ", end='')
            print("\n")
def show_answer_user(list):
    with open ("quastion.json", "r") as file:
        title = json.loads(file.read())
        return (title[list[0]][list[1]]["quastion"])


def show_split_answer(answer):
    list = (answer.split(" "))
    return list

def show_coins(list, answer_user):
    with open ("quastion.json", "r") as file:
        title = json.loads(file.read())
        if answer_user == title[list[0]][list[1]]["answer"]:
            print(f"Ответ правильный! Ты получаешь {list[1]} очков")
        else:
            print("Ответ не верный")
show_table()
answer = input("Выберите категорию и количество баллов\n")
show_split_answer(answer)
word = show_answer_user(show_split_answer(answer))
answer_user = input(f"В переводе: {word} - означает:\n")
show_coins(show_split_answer(answer), answer_user)