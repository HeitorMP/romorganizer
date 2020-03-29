from tkinter import *
from tkinter import filedialog
import os
import shutil
from collections import defaultdict

extList = ["nes", "fds"]
#path = ('/media/hmp/68C628FE738DB200/Jogos/roms/NES')
path = ('/home/hmp/NES1')
tmppath = path + '/tmp'
suffix_list = ['[', '(']
suffix = '[!]'
pos_control = 0

def refresh_list():
    print("teste")
    files_lbox.delete(0, END)
    for item in full_list_generator(path, extList):
        files_lbox.insert(END, item)


def full_list_generator(path, extlist):
    final_list = []
    files = [arq for arq in os.listdir(path) if os.path.isfile(os.path.join(path, arq))]

    for i in range(0, len(extlist)):
        files_extension = [arq for arq in files if
                           arq.lower().endswith("." + extlist[i])]  # testa se as extenções são validas
        final_list = final_list + files_extension
    final_list.sort()
    return final_list


def dict_gen(filelist):
    all_dict = {}
    filelist.sort()
    arq = ""
    for file in filelist:
        for letter in file:
            if letter == '[' or letter == '(' or letter == '.': break
            arq = arq + letter
        if arq.endswith(" "):
            arq = arq[0:-1]
        all_dict[arq] = []
        print(len(arq))
        all_dict[arq] = [file for file in filelist if file.startswith(arq) and (file[len(arq)] == ' ' or file[len(arq)] == '.')]
        arq = ""
    print(all_dict)

    final_dict_rep = {key: all_dict[key] for key in all_dict if len(all_dict[key]) > 1}
    final_dict_single = {key: all_dict[key] for key in all_dict if len(all_dict[key]) == 1}
    print(final_dict_single)
    print(final_dict_rep)
    return final_dict_rep, final_dict_single


def start_org(dict):
    if not os.path.exists(tmppath):
        try:
            os.mkdir(tmppath)
        except:
            print("Impossible to create dir")
            quit()
    print(dict)
    for key, value in dict.items():
        if len(value) <= 1: shutil.copy(path + '/' + value[0], tmppath)


def next_list(dict):
    global pos_control
    try:
        actual_key = list(dict.keys())[pos_control]
    except:
        return print('Finish')
    pos_control = pos_control + 1
    files_lbox.bind('<<ListboxSelect>>', copyselect)
    files_lbox.delete(0, END)
    for value in dict[actual_key]:
        files_lbox.insert(END, value)

def copyselect(evt):
    value = files_lbox.get(ANCHOR)
    shutil.copy(path + '/' + value, tmppath)

## pega todos os arquivos na pasta PATH e salva em file_list
file_list = full_list_generator(path, extList)
repeated_dict, single_dict = dict_gen(file_list)
root = Tk()

# path = filedialog.askdirectory()

filesLabel = Label(root, text="Files:", bg="red", fg="black")
filesLabel.pack()
buttonLabel = Label(root)
buttonLabel.pack()

leftFrame = Frame(root)
leftFrame.pack(side=LEFT, expand=YES)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

files_lbox = Listbox(leftFrame)
files_lbox.pack(fill=BOTH, expand=YES)

start_button = Button(rightFrame, text="start", command=lambda: start_org(single_dict))
next_button = Button(rightFrame, text="next", command=lambda: next_list(repeated_dict))
start_button.pack()
next_button.pack()


# lista os arquivos ao abrir o programa - sera substituido por um navegador de arquivo.
for item in file_list:
    files_lbox.insert(END, item)
# fim da listagem inicial - todas as outras vem do refresh button


root.mainloop()
