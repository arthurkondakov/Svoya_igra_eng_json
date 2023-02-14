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

with open ("quastion.json", "r") as file:
    json.loads(file)
    print(file.read)