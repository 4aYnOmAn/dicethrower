from random import randint as rd; from time import sleep

def dice():
    try:
        fn = int(input(f'[How many dices?] (num) '))
        sn = int(input(f'[Which?] (num) d'))
    except ValueError:
        print(f'[!]Not a number, try again.[!]')
        dice()
    if fn == 1:
        print(f'*Threw the dice*')
        sleep(rd(1, 3))
        return f'[Result: {fn}d{sn} = {rd(1, sn)}]\n\n'
    else:
        if fn > 999 or sn > 999:
            print(f'[!]To big number, try again, it must be < 1000[!]')
            dice()
        else:
            nums = []
            result = 0
            for i in range(fn):
                num = rd(1, sn)
                nums.append(num)
                result += num
            print(f'*Threw the dices*')
            sleep(rd(1, 3))
            return f'[Numbers: {str(nums).replace("[", "").replace("]", "")}]\n[Results: {fn}d{sn} = {result}]\n\n'

while True:
    print(dice())
