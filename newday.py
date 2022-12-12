from urllib import request
from webbrowser import open as open_browser
from sys import argv
from datetime import date

def get_day():
    day_num = date.today().day
    return str(day_num)


def make_files(day_num):
    day_str = 'day' + day_num

    open(day_str + '.txt', 'w')
    get_input(day_num, day_str+'.txt')

    with open(day_str+'.py', 'w') as f:
        f.write('\n' + '\n' + "with open('" + day_str + ".txt', 'r') as f:" + '\n    ')


def open_day_page(day):
    link = 'https://adventofcode.com/2022/day/' + day

    open_browser(link)


def get_input(day, write_to):
    link = 'https://adventofcode.com/2022/day/' + day + '/input'

    req = request.Request(link)
    req.method = 'GET'
    with open('session.txt','r') as f: session = f.read().strip()
    req.add_header('Cookie', session)
    

    with open(write_to, 'w') as f:

        with request.urlopen(req) as data:

            input = data.read().decode('UTF-8')
            f.write(input)
        

if len(argv) < 2:
    day = get_day()
    open_day_page(day)

else: day = argv[1]

make_files(day)
