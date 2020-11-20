import os, time, platform

def say(voice,message):
    os.system('clear')
    print(voice+': '+message)
    os.system('say -v '+voice+' '+message)
    time.sleep(0.5)

if __name__ == '__main__':
    v1 = 'Alice'
    v2 = 'Alex'
    if platform.system() == 'Darwin':
        f = open("Book.txt", "r")
        whichvoice = True
        for x in f:
            tmp = x.split('|')
            if tmp[0] == 'v1':
                say(v1,tmp[1])
            elif tmp[0] == 'v2':
                say(v2,tmp[1])
    else:
        print('Sorry this was built for a Mac')
