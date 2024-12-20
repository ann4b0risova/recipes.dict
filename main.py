from pprint import pprint

with open('recepty.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file.read().split('\n\n'):
        name, _, *args = line.split('\n')
        cook_li = []
        for arg in args:
            ingredient_name, quantity,  measure  = arg.split(' | ')
            cook_li.append({'ingredient_name': ingredient_name, 'quantity': int(quantity),'measure': measure})
            cook_book[name] = cook_li
    #pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count ):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Для данного блюда нет рецепта!')
    return result


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2 ))

















