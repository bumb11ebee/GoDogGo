import os, time

def say(voice,message):
    os.system('say -v '+voice+' '+message)
    time.sleep(0.5)



if __name__ == '__main__':
    v1 = 'Alice'
    v2 = 'Alex'
    f = open("Book.txt", "r")
    for x in f:
        say(v2,x)
