import json

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
tru = 0
fal = 0
sum_ = 0
def show_table():
        for category in quastion:
            print(category, end=" ")
            for point in quastion[category]:
                if quastion[category][point]["asked"] == "False":
                    print(point, end=" ")
                else:
                    print("   ", end='')
            print("\n")

def show_answer_user(list):
        return (quastion[list[0]][list[1]]["quastion"])


def show_split_answer(answer):
    list = (answer.split(" "))
    return list

def show_count_quastion():
    sum_quastion = 0
    for categ in quastion:
        for point in quastion[categ]:
            sum_quastion += 1
    return sum_quastion

def show_finish(sum_, tru, fal):
    with open ("coint.json", "w") as file:
        coins = [sum_,tru, fal]
        file.write(json.dumps(coins))
    print(f"Сумма очков {sum_}")
    print(f"Всего верных ответов {tru}")
    print(f"Нерпавильных ответов {fal}")


show_table()
count = show_count_quastion()
while count > 0:
    answer = input("Выберите категорию и количество баллов\n")
    show_split_answer(answer)
    word = show_answer_user(show_split_answer(answer))
    answer_user = input(f"В переводе: {word} - означает:\n")
    # show_coins(show_split_answer(answer), answer_user)
    if answer_user == quastion[show_split_answer(answer)[0]][show_split_answer(answer)[1]]["answer"]:
        print(f"Ответ правильный! Ты получаешь {show_split_answer(answer)[1]} очков\n")
        quastion[show_split_answer(answer)[0]][show_split_answer(answer)[1]]["asked"] = "True"
        sum_ += int(show_split_answer(answer)[1])
        tru += 1
    else:
        quastion[show_split_answer(answer)[0]][show_split_answer(answer)[1]]["asked"] = "True"
        print(f"Ответ не верный, правильный ответ {quastion[show_split_answer(answer)[0]][show_split_answer(answer)[1]]['answer']}\n")
        fal += 1
    show_table()
    count -= 1
show_finish(sum_,tru,fal)