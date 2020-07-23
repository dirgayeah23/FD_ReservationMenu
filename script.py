from food import Food
from drink import Drink

food1 = Food('Roti Lapis', 5, 330)
food2 = Food('Kue Coklat', 4, 450)
food3 = Food('Kue Sus', 2, 180)

foods = [food1, food2, food3]

drink1 = Drink('Cofee', 3, 180)
drink2 = Drink('Jus Jeruk', 2, 350)
drink3 = Drink('Espresso', 3, 30)

drinks = [drink1, drink2, drink3]

print('Food')
index = 0
for food in foods:
    print(str(index) + '. ' + food.info())
    index += 1

print('Drink')
index = 0
for drink in drinks:
    print(str(index) + '. ' + drink.info())
    index += 1

print('--------------------')

food_order = int(input('Enter food number: '))
selected_food = foods[food_order]

drink_order = int(input('Enter drink number: '))
selected_drink = drinks[drink_order]

# Ambil input dari console dan tetapkan ke variable count
count = int(input('How much food package you want? (10% discount for 3 or more): '))

# Panggil method get_total_price dari selected_food dan selected_drink
selected_food.get_total_price(count)
selected_drink.get_total_price(count)
# Cetak 'Total harga adalah $____'
result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)
print ('Total Price is $ '+str(result))
