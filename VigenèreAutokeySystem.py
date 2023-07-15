import time
import tkinter as tk
from tkinter import ttk
from unicode_tr import unicode_tr


def creatingLetterTable():
    d = 0
    for i in range(rows):
        col = []
        c = d
        for j in range(cols):
            if c > 28:
                c = 0
                col.append(letterList[c])
                c = c + 1
            else:
                col.append(letterList[c])
                c = c + 1
        letterTable.append(col)
        d = d + 1

def encryption(key,plaintext):
    ciphertext = []
    splitkey = [x for x in key]
    splitplaintext = [y for y in plaintext]
    newsplitkey =splitplaintext.copy()
    newsplitkey= generatekey(splitkey,newsplitkey)


    for i in range(len(newsplitkey)):
        ciphertext.append(letterTable[letterList.index(newsplitkey[i])][letterList.index(splitplaintext[i])])


    splitkey = "".join(newsplitkey)
    splitkey = unicode_tr(splitkey)
    ttk.Label(tab1,text=splitkey).grid(row=2, column=1)
    newciphertext = "".join(ciphertext)


    newciphertext = unicode_tr(newciphertext).upper()
    newsplitkey.clear()

    return newciphertext

def generatekey(ke,tx):

    tx1 = tx
    for i in range(len(ke)):
        tx1[i]=ke[i]

    return tx

def decryption(key,ciphertext):
    decodedplaintext = []
    splitkey= [x for x in key]

    splitciphertext = [y for y in ciphertext]
    for i in range(len(splitkey)):
        decodedplaintext.append(letterTable[0][letterTable[letterList.index(splitkey[i])].index(splitciphertext[i])])

    newplaintext = "".join(decodedplaintext)
    newplaintext = unicode_tr(newplaintext).upper()
    return newplaintext

root= tk.Tk()

letterList=['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
letterTable=[]
rows, cols=29,29

creatingLetterTable()

for i in letterTable:
    print(i)

root.title("Autokey System")
root.geometry("400x200")
tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)


tabControl.add(tab1, text='Encryption')
tabControl.add(tab2, text='Decryption')
tabControl.pack(expand=1, fill="both")


ttk.Label(tab1,text="Enter the keyword: ").grid(column=0,row=0, padx=0, pady=2)
e1=ttk.Entry(tab1)
e1.grid(column=1,row=0,pady=2)


ttk.Label(tab1,text="Enter the plain text: ").grid(column=0,row=1,padx=0,pady=2)
e2=ttk.Entry(tab1)
e2.grid(column=1,row=1,pady=2)


result = tk.StringVar(root)
ttk.Label(tab1,text="Your key is: ").grid(row =2,column=0)
ttk.Label(tab1,text="Your ciphertext is: ").grid(row =3,column=0)
ttk.Button(tab1,text="Submit",command=(lambda: result.set(encryption(e1.get().lower(),e2.get().lower())))).grid(column=4,row=1)
ttk.Label(tab1, textvariable=result,).grid(row=3, column=1)


ttk.Label(tab2,text="Enter the key: ").grid(column=0,row=0, padx=0, pady=2)
e3=ttk.Entry(tab2)
e3.grid(column=1,row=0,pady=2)


ttk.Label(tab2,text="Enter the chipher text: ").grid(column=0,row=1,padx=0,pady=2)
e4=ttk.Entry(tab2)
e4.grid(column=1,row=1,pady=2)


result2 = tk.StringVar(root)
ttk.Label(tab2,text="Your decodedtext is: ").grid(row =2,column=0)
ttk.Button(tab2,text="Submit",command=(lambda: result2.set(decryption(e3.get().lower(),e4.get().lower())))).grid(column=4,row=1)
ttk.Label(tab2, textvariable=result2).grid(row=2, column=1)


root.mainloop()








