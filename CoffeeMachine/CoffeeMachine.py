import random

milk = random.randint(2000, 5000)
beans = random.randint(150, 500)
clean_cup = random.randint(5, 15)
water_per_cup = 0
milk_per_cup = 0
beans_per_cup = 0
price = 0
all_portion = 0
money = random.randint(500, 1000)
water = random.randint(5000, 10000)


class CoffeeMachine:
    def __init__(self, buy, fill, take, remaining, close):
        global water, milk, beans, clean_cup, water_per_cup, milk_per_cup, beans_per_cup, price, money, all_portion
        water_per_cup = 0
        milk_per_cup = 0
        beans_per_cup = 0
        price = 0
        self.buy = buy
        self.fill = fill
        self.take = take
        self.remaining = remaining
        self.close = close


option = CoffeeMachine('buy', 'fill', 'take', 'remaining', 'exit')


def Option():
    global water_per_cup, milk_per_cup, beans_per_cup, water, milk, beans, money, all_portion, clean_cup
    choose = str(input(f'Write action (buy, fill, take, remaining, exit)\n>>> '))
    if choose == option.buy:
        Buy()
    elif choose == option.fill:
        Fill()
    elif choose == option.take:
        Take()
    elif choose == option.remaining:
        Remaining()
    elif choose == option.close:
        print('GoodBye!')
    else:
        print('Try Again!')


def Buy():
    global water_per_cup, milk_per_cup, beans_per_cup, water, milk, beans, all_portion, price
    choose = int(input(f'What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino ||  0 - Main Menu\n>>> '))
    if choose == 1:
        water_per_cup = 250
        milk_per_cup = 16
        beans_per_cup = 0
        price = 4
        Machine()
    elif choose == 2:
        water_per_cup = 350
        milk_per_cup = 75
        beans_per_cup = 20
        price = 7
        Machine()
    elif choose == 3:
        water_per_cup = 200
        milk_per_cup = 100
        beans_per_cup = 12
        price = 6
        Machine()
    elif choose == 0:
        Option()
    else:
        print('Try Again!')
        Buy()


def Machine():
    global water_per_cup, milk_per_cup, beans_per_cup, water, milk, beans, price, all_portion, money, clean_cup
    print(f'You will be given a first clean glass for each coffee.')
    ingredients = list([water, milk, beans])
    ingredients2 = list([water, milk])
    minimum = min(ingredients)
    minimum2 = min(ingredients2)
    cup = int(input(f'Write how many cups of coffee you will need:\n>>> '))
    if water_per_cup * cup > water:
        print('Sorry, not enough water')
        choose = int(input(f'Do u wanna fill?  1 - Yes  ||  2 - Choose another quantity\n>>> '))
        if choose == 1:
            Fill()
        elif choose == 2:
            Buy()
    elif milk_per_cup * cup > milk:
        print('Sorry, not enough milk')
        choose = int(input(f'Do u wanna fill?  1 - Yes  ||  2 - Choose another quantity\n>>> '))
        if choose == 1:
            Fill()
        elif choose == 2:
            Buy()
    elif beans_per_cup * cup > beans:
        print('Sorry, not enough beans')
        choose = int(input(f'Do u wanna fill?  1 - Yes  ||  2 - Choose another quantity\n>>> '))
        if choose == 1:
            Fill()
        elif choose == 2:
            Buy()
    elif cup > clean_cup:
        print('Sorry, not enough disposable cups')
        choose = int(input(f'Do u wanna fill?  1 - Yes  ||  2 - Choose another quantity\n>>> '))
        if choose == 1:
            Fill()
        elif choose == 2:
            Buy()

    else:
        print('I have enough resources, making you a coffee!')
        if minimum == ingredients[0]:
            all_portion = int(water / water_per_cup)

        elif minimum == ingredients[1]:
            all_portion = int(milk / milk_per_cup)
        elif beans_per_cup <= 0 and minimum == ingredients[2]:
            if minimum2 == ingredients2[0]:
                all_portion = int(water / water_per_cup)
            if minimum2 == ingredients2[1]:
                all_portion = int(milk / milk_per_cup)
        elif beans_per_cup > 0 and minimum == ingredients[2]:
            all_portion = int(beans / beans_per_cup)
        can_cup = all_portion - cup

        choose = int(input(f'''
Yes, I can make that amount of coffee (and even {can_cup} more than that.)
Are you sure you want {cup} servings?
---------It cost {price * cup}!---------
1 - Yes  ||  2 - Choose amount\n>>> '''))
        if choose == 1:
            get_money = int(input(f'Contribute money\n>>> '))
            cost_portion = price * cup
            money_back = get_money - cost_portion
            if get_money >= cost_portion:
                money = money + get_money - money_back
                print(f'''
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!               
Your surrender is {get_money - cost_portion} UAH!
''')
                water = water - int(cup * water_per_cup)
                milk = milk - int(cup * milk_per_cup)
                if beans_per_cup > 0:
                    beans = beans - int(cup * beans_per_cup)
                clean_cup = clean_cup - cup
                Option()
            elif get_money < cost_portion:
                question = int(input(f'''
Money not enough! Money back ({get_money})
Do u wanna try again?  1 - Yes  ||  2 - Main Menu\n>>> '''))
                if question == 1:
                    Buy()
                elif question == 2:
                    Option()
        elif choose == 2:
            Buy()


def Fill():
    global water, milk, beans, clean_cup, money
    print(f'''{water} of water  |  {milk} of milk  |  {beans} of coffee beans  |  {clean_cup} of disposable cups''')
    choose = int(input(f'Do u wanna add ingredients?  1 - Add | 2 - Main Menu\n>>> '))
    if choose == 1:
        water_add = int(input(f'Write how many ml of water do you want to add:\n>>> '))
        water = water_add + water
        milk_add = int(input(f'Write how many ml of milk do you want to add:\n>>> '))
        milk = milk_add + milk
        beans_add = int(input(f'Write how many grams of coffee beans do you want to add:\n>>> '))
        beans = beans_add + beans
        add_clean_cup = int(input(f'Write how many disposable cups of coffee do you want to add:\n>>> '))
        clean_cup = add_clean_cup + clean_cup
        add_money = int(input(f'Write how many of money do you want to add:\n>>> '))
        money = add_money + money
        print(f'''{water} of water  |  {milk} of milk  |  {beans} of coffee beans  |  {clean_cup} of disposable cups''')
        choose = int(input(f'Do u wanna add more ingredients?  1 - Yes  | 2 - Main Menu\n>>> '))
        if choose == 1:
            Fill()
        if choose == 2:
            Option()
    if choose == 2:
        Option()


def Take():
    global money
    print(f'Money in bank: {money}')
    choose = int(input(f'Do u wanna take money?  1 - Yes  ||  2 - Main Menu\n>>> '))
    if choose == 1:
        if money == 0:
            print('no money')
            Take()
        elif money > 0:
            money = money - money + 1000
            print('Money received successfully')
            Take()
    elif choose == 2:
        Option()


def Remaining():
    global water, milk, beans, clean_cup
    print(f'''The coffee machine has:
{water} of water  |  {milk} of milk  |  {beans} of coffee beans  |  {clean_cup} of disposable cups  |  {money} of money
''')
    choose = int(input(f'Do u wanna add ingredients?  1 - Add ingredients  | 2 - Main Menu\n>>> '))
    if choose == 1:
        Fill()
    if choose == 2:
        Option()


Option()