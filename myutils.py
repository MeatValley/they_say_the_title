from turtle import position

def get_s0xe0y(i):
    if (i%10 == 0):
        s0xe0y = 'S0'+str(int(i/10))+'E10'
    else:
        s0xe0y = 'S0'+str(int(i/10 + 1))+'E0'+ str(i%10)
    return s0xe0y

def generate_the_subtitle_name(i):
    """generate the title based on the number"""
    if (i%10 == 0):
        title = 'Game.Of.Thrones.S0'+str(int(i/10))+'E10.srt'
    else:
        title = 'Game.Of.Thrones.S0'+str(int(i/10 + 1))+'E0'+ str(i%10)+'.srt'
    return title

def generate_the_path(title, i):
    if (i%10 == 0):
        path ='subtitles/s'+ str(int(i/10))+'/'+title

    else:
        path ='subtitles/s'+ str(int(i/10+1))+'/'+title

    return path


def find_the_ep_title():
    """this function receive a file and return the title of that file"""
    titles = []
    #s1
    for i in range(1,10):
        title = generate_the_subtitle_name(i)
        path = generate_the_path(title, i)
        f = open(path)
        x = f.read()
        # for c in x:
        #     if c == '<font color=#00FFFF>':
        c = ''
        for i in range (240, 400): 
            if x[i] == 'F' and x[i+1] == '>':
                for j in range(100):
                    # print(x[i+j+2], end='')
                    c+=x[i+j+2]
                    if x[i+j+3] == '<':
                        break
                titles.append(c)
                break
        
            
        print('')
    # print(titles)

    f = open('titles.txt', "w")
    for title in titles:
        f.write(title+'\n')
    f.close

    
def find_all(str, key):
    start = 0
    positions = []
    count = 0
    c = 0
    while(start != -1):
        x = str.find(key, start)
        count+=1
        if x!=-1:
            positions.append(x)
            start=x+len(key)
            c+=1
        if(start>(len(str)-1) or start == 0 or count==5):
            start =-1

        # print(start)
    return positions, c

import linecache as lc


def serach_with_getline(file, key):
    line = 0
    f = open(file, "r")
    flag = False
    quote = ''
    # print(f)
    for i in f:
        k = i.replace('\n', '')
        k = k.lower()
        x = k.find(key)
        if(x!=-1):
            # print(k)
            quote = k
            flag = True
            time = lc.getline(file, line)
            # print(time)
        line+=1
    return flag, quote




