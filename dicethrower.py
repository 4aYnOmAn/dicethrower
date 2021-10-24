from random import randint as rd; from time import sleep as sl; from subprocess import check_output as cho


##For more clear code and visuals (FMCCV)
clear = cho("clear").decode("utf-8")


##FMCCV
def good_print(text):
    return cho(["figlet", text]).decode("utf-8")


### !!!WARNING!!! ###
### DOG SHIT CODE ###
### WITH RU COMMS ###
def loadthing(time, times, sn, en):
    print(clear)
    endtimes = 0
    
    ## Сколько раз уже прокрутилась кость
    for n in range(0, times):
        
        ## Какие числа на кости прокрутились
        for i in range(1, sn+1):
            
            ## Если кость уже сделала как минимум кол-во заданных кругов
            ## И число на ней совпадает с окончательным числом
            if endtimes > times and i == en:
                
                ## Принт его
                print(good_print(f"[ {en} ]")); sl(time+1); print(clear)
                return
                
            ## Если нет то пох
            print(good_print(f"[ {i} ]")); sl(time); print(clear)
            
            ## Плюс один круг
            endtimes +=1
        time += 0.1


##Main func
def dice():
    
    ##Inputs
    try:
        fn = int(input(f'[How many dices?] (num) '))
        sn = int(input(f'[Which?] (num) d'))
    except ValueError:
        return '[!]Not a number, try again.[!]\n\n'
    
    ##If 1 dice
    if fn == 1:
        
        ##If not much sides == good visuals
        if sn <= 100:
            en = rd(1, sn)
            loadthing(10/sn*0.1, rd(1, sn), sn, en)
            return '[Results]:\n' + good_print(f'{fn}d{sn} = {en}\n\n')
        
        ##Else == fuck you, here's your rd(1, sn) and nothing else
        else:
            print(clear)
            return '[Results]:\n' + good_print(f'{fn}d{sn} = {rd(1, sn)}\n\n')
    
    ##If more
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
