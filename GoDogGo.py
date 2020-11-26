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
        #If this is a Macbook then open the file
        f = open("Book.txt", "r") #reads the words in the book

        for each_line in f:
            tmp = each_line.split('|')#Splits the line into a voice and a sentence
            if tmp[0] == 'v1': #if the voice is v1 then read the line as v1
                say(v1,tmp[1])
            elif tmp[0] == 'v2': #if the voice is v2 then read the line as v2
                say(v2,tmp[1])
    else:
        print('Sorry this was built for a Mac')
