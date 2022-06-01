# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 11:13:01 2022

@author: marti
"""

import tkinter as tk
app = tk.Tk()
app.title("La deuxième calculatrice de Floriane")
app.geometry("245x290")
app.minsize(245, 290)


#Les fonctions pour les menus
def showHelp():
    shelp = tk.Toplevel(app)
    label = tk.Label(shelp, text="Ceci est une aide")
    shelp.geometry("200x150")
    label.pack()

def quitfunc():
    app.destroy()
    


#Les fonctions pour les chiffres
def btn0(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"0")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"0")
    print(resLeft.get())
    print(resRight.get())
 
def btn1(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"1")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"1")
    print(resLeft.get())
    print(resRight.get())
   
def btn2(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"2")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"2")
    print(resLeft.get())
    print(resRight.get())
    
def btn3(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"3")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"3")
    print(resLeft.get())
    print(resRight.get())
    
def btn4(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"4")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"4")
    print(resLeft.get())
    print(resRight.get())
    
def btn5(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"5")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"5")
    print(resLeft.get())
    print(resRight.get())
    
def btn6(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"6")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"6")
    print(resLeft.get())
    print(resRight.get())
    
def btn7(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"7")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"7")
    print(resLeft.get())
    print(resRight.get())
    
def btn8(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"8")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"8")
    print(resLeft.get())
    print(resRight.get())
    
def btn9(*args):
    print("varMode =", varMode.get())
    if varMode.get()==0:
        resLeft.set(str(resLeft.get())+"9")
    elif varMode.get()==1:
        resRight.set(str(resRight.get())+"9")
    print(resLeft.get())
    print(resRight.get())

#Les fonctions pour les calculs

def btnPlus(*args):
    if resFinal.get()!=0 :    #On utilise ceci pour savoir si il y a déjà eu un calcul d'effectuer afin de pouvoir enchainer les calculs 
        resLeft.set(resFinal.get())
    varCalcul.set("+")
    varMode.set(1)
    print("Variable de calcul: ", varCalcul.get())
    print("Variable de mode: ", varMode.get())
   
def btnMoins(*args):
    if resFinal.get()!=0 :
        resLeft.set(resFinal.get())
    varCalcul.set("-")
    varMode.set(1)
    print("Variable de calcul: ", varCalcul.get())
    print("Variable de mode: ", varMode.get())

def btnMult(*args):
    if resFinal.get()!=0 :
        resLeft.set(resFinal.get())
    varCalcul.set("*")
    varMode.set(1)
    print("Variable de calcul: ", varCalcul.get())
    print("Variable de mode: ", varMode.get())
    
def btnDiv(*args):
    if resFinal.get()!=0 :
        resLeft.set(resFinal.get())
    varCalcul.set("/")
    varMode.set(1)
    print("Variable de calcul: ", varCalcul.get())
    print("Variable de mode: ", varMode.get())
    
def btnEgal(*args):
    if varCalcul.get()=="+" :
        resFinal.set(float(resLeft.get()) + float(resRight.get()))
        print(resFinal.get())
    elif varCalcul.get()=="-" :
        resFinal.set(float(resLeft.get()) - float(resRight.get()))
        print(resFinal.get())
    elif varCalcul.get()=="*" :
        resFinal.set(float(resLeft.get()) * float(resRight.get()))
        print(resFinal.get())
    elif varCalcul.get()=="/" :
        resFinal.set(float(resLeft.get()) / float(resRight.get()))
        print(resFinal.get())
    else:
        print(resFinal.get())
        
    resLeft.set("")
    resRight.set("")
    varCalcul.set("")
    varMode.set(0)
    
def btnC(*args):
    resLeft.set("")
    resRight.set("")
    varCalcul.set("")
    varMode.set(0)
    resFinal.set(0)

    
#Définition des variables
resLeft = tk.StringVar()
varCalcul = tk.StringVar()
varMode = tk.IntVar()
resRight = tk.StringVar()
resFinal = tk.DoubleVar()

#Définition des menus
mainmenu = tk.Menu()
menu1 = tk.Menu(mainmenu, tearoff=0)
menu1.add_command(label="Option 1")
menu1.add_command(label="Option 2")

menu2 = tk.Menu(mainmenu, tearoff=0)
menu2.add_command(label="Help", command=showHelp)
menu2.add_command(label="Quit", command=quitfunc)

mainmenu.add_cascade(label="Menu 1", menu=menu1)
mainmenu.add_cascade(label="Menu 2", menu=menu2)

#Définition des frames
frame0 = tk.Frame(app, padx=10, pady=10)
frame0.pack(expand=1)
frame1 = tk.LabelFrame(frame0, text="Ecran", padx=20, pady=20)
frame1.grid(row=0, columnspan=3)
frame2 = tk.LabelFrame(frame0, text="Boutons", padx=10, pady=10)
frame2.grid(row=3, column=1)

#Définition du label frame1

afficher = tk.Label(frame1, textvariable=resFinal, width=25).grid(columnspan=4)

#Définition des boutons frame2
bouton0 = tk.Button(frame2, text="   0   ", command = btn0, relief="raised").grid(row=3, column=1, padx=5, pady=5)
bouton1 = tk.Button(frame2, text="   1   ", command = btn1).grid(row=0, column=0, padx=5, pady=5)
bouton2 = tk.Button(frame2, text="   2   ", command = btn2).grid(row=0, column=1, padx=5, pady=5)
bouton3 = tk.Button(frame2, text="   3   ", command = btn3).grid(row=0, column=2, padx=5, pady=5)
bouton4 = tk.Button(frame2, text="   4   ", command = btn4).grid(row=1, column=0, padx=5, pady=5)
bouton5 = tk.Button(frame2, text="   5   ", command = btn5).grid(row=1, column=1, padx=5, pady=5)
bouton6 = tk.Button(frame2, text="   6   ", command = btn6).grid(row=1,  column=2, padx=5, pady=5)
bouton7 = tk.Button(frame2, text="   7   ", command = btn7).grid(row=2, column=0, padx=5, pady=5)
bouton8 = tk.Button(frame2, text="   8   ", command = btn8).grid(row=2, column=1, padx=5, pady=5)
bouton9 = tk.Button(frame2, text="   9   ", command = btn9).grid(row=2,  column=2, padx=5, pady=5)
bouton10 = tk.Button(frame2, text="   +   ", command = btnPlus).grid(row=0, column=3, padx=5, pady=5)
bouton11 = tk.Button(frame2, text="   -   ", command = btnMoins).grid(row=1, column=3, padx=5, pady=5)
bouton12 = tk.Button(frame2, text="   x   ", command = btnMult).grid(row=2, column=3, padx=5, pady=5)
bouton13 = tk.Button(frame2, text="   /   ", command = btnDiv).grid(row=3, column=3, padx=5, pady=5)
bouton14 = tk.Button(frame2, text="   =   ", command = btnEgal).grid(row=3, column=2, padx=5, pady=5)
bouton15 = tk.Button(frame2, text="   C   ", command = btnC).grid(row=3, column=0, padx=5, pady=5)


#Lancement de la fenêtre principale
app.config(menu=mainmenu)
app.mainloop()