from tkinter import *
from tkinter import Menu
from tkinter import filedialog
from time import sleep

vars = ['послед', 0]
output_mode = 1
output_path = ""

def manage_input(command, ignore=-1):
    fields = []
    for x in range(1, len(command)):
        if x == ignore:
            continue
        else:
            if command[x][0] == "$":
                i = vars.index(command[x][1:])
                fields.append(int(vars[i + 1]))
            else:
                fields.append(int(command[x]))
    return fields

def manage_output(output):
    if output_mode == 0:
        out.configure(text=output)
    elif output_mode == 2:
        with open(output_path, "w") as file:
            file.write(str(output))

def manage_path(path):
    out = path.replace("|", " ")
    return out

def ask_file():
    file = filedialog.askopenfile()
    run_by_file(file, 1)

def run_by_file(path, mode=0):
    if mode == 0:
        path = manage_path(path)
        with open(path, "r") as file:
            data = file.readlines()
    else:
        data = path.readlines()
    for line in data:
        exec(1, line)
        sleep(0.1)

def clear_data():
    global vars
    vars = ["послед", 0]

def manage_load_config():
    global output_mode
    global output_path
    with open("config.txt", "r") as file:
        data = file.readlines()
    for _ in range(0, len(data)):
        line = list(data[_].split())
        if line[0] == "output_mode":
            output_mode = int(line[1])
        elif line[0] == "output_path":
            output_path = manage_path(line[1])
    
    print(output_path, output_mode)

def exec(mode=0, line=''):
    if mode == 0:
        command = list(inpt.get().split())
    elif mode == 1:
        command = list(line.split())
    if command[0] == 'сум':
        sm = 0
        ipt = manage_input(command)
        for _ in ipt:
            sm += int(_)
        manage_output(sm)
        vars[1] = str(sm)
    elif command[0] == "разн":
        ipt = manage_input(command)
        manage_output(int(ipt[0])-int(ipt[1]))
        vars[1] = str(int(ipt[0])-int(ipt[1]))
    elif command[0] == "перем":
        ipt = manage_input(command, ignore=1)
        if command[1] not in vars:
            vars.append(command[1])
            vars.append(ipt[0])
        else:
            i = vars.index(command[1])
            vars[i+1] = ipt[0]
    elif command[0] == "эхо":
        ipt = manage_input(command)
        manage_output(ipt[0])
    elif command[0] == "запуск":
        run_by_file(command[1])
    elif command[0] == "умнож":
        ipt = manage_input(command)
        manage_output(ipt[0]*ipt[1])
    elif command[0] == "дел":
        ipt = manage_input(command)
        if ipt[1] == 0:
            manage_output("деление на ноль")
        else:
            manage_output(ipt[0]//ipt[1])
    elif command[0] == "степень":
        ipt = manage_input(command)
        manage_ouput(ipt[0]**ipt[1])

manage_load_config()
main = Tk()
main.title("КОНСОЛЬ RUSH")
menu = Menu(main)  
menu.add_command(label='Открыть...', command=ask_file)
menu.add_command(label='Очистить данные', command=clear_data)
main.config(menu=menu)  
#main.geometry("150x35")
btn = Button(main, text="ОТПРАВИТЬ", command=exec)
btn.grid(column=1, row=0)
inpt = Entry(main, width=50)
inpt.grid(column=0, row=0) 
lbl = Label(text="ВЫВОД: ")
lbl.grid(column=0, row=1)
out = Label(text="")
out.grid(column=0, row=2)

main.mainloop()
