def create_cook_book():
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            dish = line.strip().lower()
            ingridients = []
            index = int(f.readline().strip())
            for i in range(index):
                ingridient_name = f.readline().strip().split('|')
                cook_ingredient = {'ingridient_name': ingridient_name[0], 'quantity': int(ingridient_name[1]),
                                  'measure': ingridient_name[2]}
                ingridients.append(cook_ingredient)
            f.readline()
            cook_book.update({dish: ingridients})
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = create_cook_book()
    new_ingridient = ''
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = ingridient
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                new_ingridient = ingridient.pop('ingridient_name')
                shop_list[new_ingridient] = new_shop_list_item
            else:
                shop_list[new_ingridient]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
      for shop_list_item, ingridients in shop_list.items():
        print(f'Вам понадобится {shop_list_item} {ingridients["quantity"]} {ingridients["measure"]}')


def create_shop_list():
    try:
        person_count = int(input('Введите количество человек: '))
        dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
        shop_list = get_shop_list_by_dishes(dishes, person_count)
        print_shop_list(shop_list)
    except:
        print('Не знаем такого блюда, вот варианты которые можно посчитать:')
        print(*create_cook_book().keys(), sep=', ')

create_shop_list()