# работа с файлами
import pprint
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
#
# for key, val in cook_book.items():
#     print(f'{key}:')
#     for element in val:
#         print(f'{element}')

shop_list = {}


def get_shop_list_by_dishes(dishes, person_count):
    for dish in dishes:
        if dish in cook_book:
            for i in range((len(cook_book[dish]))):
                if not cook_book[dish][i]['ingredient_name'] in shop_list:
                    ingridient_quantity = cook_book[dish][i]['quantity'] * person_count
                else:
                    ingridient_quantity = shop_list[cook_book[dish][i]['ingredient_name']]['quantity'] + \
                                          cook_book[dish][i]['quantity'] * person_count

                in_list = {'measure': cook_book[dish][i]['measure'],
                           'quantity': ingridient_quantity}
                shop_list[cook_book[dish][i]['ingredient_name']] = in_list
    return shop_list


# get_shop_list_by_dishes(["Омлет", "Фахитос"], 2)
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(shop_list)
