# работа с файлами

cook_book = {}

def linepackagetodict(linelist):
    meal_book = {}
    meal_book["ingredient_name"] = linelist[0]
    meal_book["quantity"] = int(linelist[1])
    meal_book["measure"] = linelist[2]
    return meal_book

with open('recipebook.txt') as f:
    for line in f:
        rl = line.strip()
        if not rl.isdigit() and not "|" in rl and not rl == "":
            meal = rl
            cook_book[rl] = []
        elif "|" in rl:
            list_rl = rl.split(" | ")
            cook_book[meal].append(linepackagetodict(list_rl))

for key,val in cook_book.items():
    print(f'{key}:')
    for element in val:
        print(f'{element}')
