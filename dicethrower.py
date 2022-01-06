from random import randint as rd
from time import sleep as sl
from subprocess import check_output as cho


clear = cho("clear").decode("utf-8")


def good_print(text):
    return cho(["figlet", text]).decode("utf-8")


def loadthing(time, times, sn, en):
    print(clear)
    endtimes = 0
    for n in range(0, times):
        for i in range(1, sn+1):
            if endtimes > times and i == en:
                print(good_print(f"[ {en} ]")); sl(time+1); print(clear)
                return
            print(good_print(f"[ {i} ]")); sl(time); print(clear)
            endtimes +=1
        time += 0.1


def dice():
    try:
        fn = int(input(f'[How many dices?] (num) '))
        sn = int(input(f'[Which?] (num) d'))
    except ValueError:
        return '[!]Not a number, try again.[!]\n\n'
    if fn == 1:
        if sn <= 100:
            en = rd(1, sn)
            loadthing(10/sn*0.1, rd(1, sn), sn, en)
            return '[Results]:\n' + good_print(f'{fn}d{sn} = {en}\n\n')
        else:
            print(clear)
            return '[Results]:\n' + good_print(f'{fn}d{sn} = {rd(1, sn)}\n\n')
    else:
        if fn > 999 or sn > 999:
            return '[!]To big number, try again, it must be < 1000[!]\n\n'
        else:
            nums = []
            result = 0
            for i in range(fn):
                num = rd(1, sn)
                nums.append(num)
                result += num
            return f'[Numbers: {str(nums).replace("[", "").replace("]", "")}]\n' + '[Result]:\n' + good_print(f'{fn}d{sn} = {result}\n\n')

        
while True:
    try:
        print(clear)
        print(dice())
        input('[Waiting for any input...]')
    except KeyboardInterrupt:
        print("[^C pressed, exiting...]")
        exit()
