print("""Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!""")
water = 200
milk = 50
coffee = 15

a = int(input("Write how many cups of coffee you will need:"))
b = str(input("Write your favorite coffee:"))

if a == 1:
    print("For " + str(a) + " cup of coffee you will need:")
    print('water ' + str(water) + ' ml')
    print('milk ' + str(milk) + ' ml')
    print('coffee ' + str(coffee) + ' g')
elif a > 1:
    print("For " + str(a) + " cups of coffee you will need:")
    print('water ' + str(a * water) + ' ml')
    print('milk ' + str(a * milk) + ' ml')
    print('coffee ' + str(a * coffee) + ' g')

print("What is your favorite coffee?")
my_list = ['americano', 'cappuccino', 'espresso', 'latte']
if b == 'americano':
    else
