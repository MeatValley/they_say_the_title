from re import sub
import myutils as m
import linecache as lc

t = open('titles.txt')
they_say_it = open ("they_say_it.txt", "w")
for i in range (1,39):
    they_say_it = open ("they_say_it.txt", "a")
    x = -1

    title = m.generate_the_subtitle_name(i)
    path = m.generate_the_path(title, i)

    current_title = t.readline()
    current_title= current_title.lower()
    current_title= current_title.replace('\n', '')

    time= '\n'
    line = '\n'+m.get_s0xe0y(i) + ' Title: '+ current_title + '\nthey say it?' 
    got_line='\n\nBonus: They say \'game of thrones\' \o/ '

    f = open(path)
    flag = False
    line_counter = 1
    got = -1
    got_flag = False
    for i in f:
        current_line = i.replace('\n', '')
        current_line = current_line.lower()
        x = current_line.find(current_title)
        got = current_line.find('game of thrones')
        if got != -1:

            # print(got_line)
            if (current_line.find('font color') == -1 ):
                got_time = lc.getline(path, line_counter-1)
                got_quote = current_line
                got_line+= '\nline: ' + got_quote + '\nwhen? in ' + got_time
                got_flag = True

        if(x!=-1):
            if not flag: line = line + '  YES!'+'\n\n'
            line+='quote: ' + current_line
            time = lc.getline(path, line_counter-1)
            if(time[0] != '0'):
                time = lc.getline(path, line_counter-2)
            line += '\nWhen? '+ time+ '\n'
            flag = True
        line_counter+=1


    if not flag:
        #maybe is the title is splited in two 
        part_of_title = ''
        for i in range(7):
            part_of_title += current_title[i]

        # print(part_of_title)
        fl, quote2 = m.serach_with_getline(path, part_of_title)

        line +='  Nop :(\n'
        
        if fl:
            line += 'At least they say "' + part_of_title + '"'
            line+= '\nin: '+ quote2

    if got_flag:
        print('12')
        line+=got_line
    
    they_say_it.write('\n--------------------------')
    they_say_it.write(line)

