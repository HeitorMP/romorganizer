from tkinter import *
from tkinter import filedialog
import os
import re
from collections import defaultdict

extList = ["nes", "fds"]
#path = ('/media/hmp/68C628FE738DB200/Jogos/roms/NES')
path = ('/home/hmp/NES1')
suffix_list = ['[', '(']
suffix = '[!]'

def refresh_list():
    print("teste")
    files_lbox.delete(0, END)
    for item in full_list_generator(path, extList):
        files_lbox.insert(END, item)


def full_list_generator(path, extlist):

    final_list = []
    files = [arq for arq in os.listdir(path) if os.path.isfile(os.path.join(path, arq))]

    for i in range(0, len(extlist)):
        files_extension = [arq for arq in files if arq.lower().endswith("." + extlist[i])] # testa se as extenções são validas
        final_list = final_list + files_extension

    final_list.sort()
    return final_list

def locate_equals(filelist):
    repeated_dict = {}
    filelist.sort()
    arq = ""
    for file in filelist:
        for letter in file:
            if letter == '[' or letter == '(' or letter == '.' : break
            arq = arq + letter
        if arq.endswith(" "): arq = arq[0:-1]
        repeated_dict[arq] = [file for file in filelist if file.startswith(arq)]
        arq = ""

    final_dict = {key: repeated_dict[key] for key in repeated_dict if len(repeated_dict[key]) > 1}

    return final_dict

file_list = full_list_generator(path, extList)
root = Tk()

#path = filedialog.askdirectory()

filesLabel = Label(root, text="Files:", bg="red", fg="black")
filesLabel.pack()
buttonLabel = Label(root)
buttonLabel.pack()

leftFrame = Frame(root)
leftFrame.pack(side=LEFT)

rightFrame = Frame(root)
rightFrame.pack(side=RIGHT)

files_lbox = Listbox(leftFrame)
files_lbox.pack(side=TOP)

refresh_button = Button(rightFrame, text="refresh", command=refresh_list)
refresh_button.pack()



#lista os arquivos ao abrir o programa - sera substituido por um navegador de arquivo.
for item in file_list:
    files_lbox.insert(END, item)
#fim da listagem inicial - todas as outras vem do refresh button

key = '4 Nin Uchi Mahjong'
teste = locate_equals(file_list)
print(teste)


root.mainloop()

