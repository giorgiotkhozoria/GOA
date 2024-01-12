import random
inp = input("waht is ure name?: ")

for i in range(6):
        you = random.randint(1,6)
        comp = random.randint(1,6)

        if you > comp:
                print(f"You won!! {inp}")
        elif you < comp:
                print(f"You loose!!{inp}")
        else:
                print('Draw{}'.format(inp))