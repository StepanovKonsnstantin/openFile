from pprint import pprint

with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book= {}
    for line in file:
        recipes_name = line.strip()
        # print(recipes_name)
        number_of_components = int(file.readline().strip())
        # print(number_of_components)
        components = []
        for _ in range(number_of_components):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            components.append({
                'ingredient_name' : ingredient_name,
                'quantity' : quantity,
                'measure' : measure
            })
        file.readline()
        cook_book[recipes_name] = components
new_book = {}
def get_shop_list_by_dishes(dishes, person_count): 
  for name in dishes:
    name_product = cook_book.get(name)
    for ing in name_product:
      # print(ing)
      ing['quantity'] = int(ing.get('quantity') * person_count)
      name_ing = ing.pop('ingredient_name')
      new_book[name_ing] = ing
    # pprint (new_book)
    return pprint(new_book)
  
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# person_count = int(input('Введите количество персон '))
# print(cook_book)
# def get_shop_list_by_dishes(dishes, person_count):
#     for name in dishes:
#         grocery_list = cook_book.get(name)
#         for products in grocery_list:
#             print(products)
#             name_produts = products.get('ingredient_name')
#             print(name_produts)
#             # for i in products:
#                 # print(i)
#         # print(grocery_list)
# get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


