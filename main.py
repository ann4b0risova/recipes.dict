cook_book = {}
with open('recepty.txt', encoding='utf-8') as file:
    for line in file.read().split('\n\n'):
        name, _, *args = line.split('\n')
        cook_li = []
        for arg in args:
            ingredient_name, quantity,  measure  = arg.split(' | ')
            cook_li.append({'ingredient_name': ingredient_name, 'quantity': int(quantity),'measure': measure})
            cook_book[name] = cook_li
print(cook_book)












