# This code is written by Alpha__830 # Please check my github and use my code with credit This script is a time
# counter and you can use it to count the minutes and seconds you want, understanding this code is very easy and
# Don't forget to have fun See you all in another script
# AlPHA__830 :)

try:
    from time import sleep
    import os
    from win10toast import ToastNotifier
    from termcolor import colored
except:
    print("There is an Error opening modules Please check if you have all of the modules installed")
count = input(colored("Please enter Timer time\n",'blue'))

if count == ':':
    pass
else:
    count = count.replace(';','')
    count = count.replace(',','')
    leng = len(count)
    count_sep = ':'.join(count[i:i +2] for i in range(0,4,2))

def convert():
    count_c = list(count_sep.split(":"))
    if int(count_c[0]) <= 60 and int(count_c[1]) <= 60:
        sleep(0.5)
    else:
        exit()
    return count_c

def min_t_sec():
    global min_se
    count_c = convert()
    min = 60
    f = int(count_c[0]) * min
    b = int(count_c[1])
    min_se = f + b
    return min_se

def countdown(sec):
    min_se = min_t_sec()
    while sec:
        mins, secs = divmod(sec, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\n")
        sleep(1)
        sec -= 1
        if sec == False:
            notif = ToastNotifier()
            title = "Timer ended"
            message = "END of Timer, We reach " + count_sep
            notif.show_toast(title,message,duration=30)
            sleep(1)
            exit()
        else:
            pass

try:
    min_t_sec()
    countdown(min_se)
except:
    print("There is Error at the end of the code Please check it out")
