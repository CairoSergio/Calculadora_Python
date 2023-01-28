from tkinter import *
from tkinter import ttk

Calculadora = Tk()
Calculadora.title("Calculadora")
Calculadora.geometry('320x505')
Calculadora.resizable(height=False,width= False)

Tela_resultados = Frame(Calculadora,width=350, height=80, bg='#00c3cd')
Tela_resultados.grid(column=0, row=0)

conta = ''
def inserir(text):
    global conta

    conta = conta + str(text) 
    resultado.set(conta)

resultado = StringVar()

def dell_all():
    global resultado
    global conta
    conta = ''
    resultado.set('')
def dell():
    global conta
    global resultado

    dell = conta[:-1]
    conta =dell
    resultado.set(str(dell))
def calcular ():
    global resultado
    global conta
    resultado.set(str(eval(conta)))
    cont = str(eval(conta))
    conta =cont
resultados_lab = Label(Tela_resultados,justify=RIGHT,font=('Ivy 26'), textvariable=resultado, fg="#fff",bg='#00c3cd', anchor='e',width=16, height=2)
resultados_lab.place(x=0, y=0)

butao_C = Button(text="C",width=8,height=4,relief=RAISED, font="15",overrelief="ridge", command=dell_all)
butao_C.place(x=0,y=80)
butao_del = Button(text="DEL",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=dell)
butao_del.place(x=80,y=80)
butao_per = Button(text="%",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("%"))
butao_per.place(x=160,y=80)
butao_div = Button(text="/",width=8,bg='#Fa2',fg='#fff',height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("/"))
butao_div.place(x=240,y=80)

butao_9 = Button(text="9",width=8,height=4,relief='raised', font="15",overrelief="ridge", command=lambda: inserir("9"))
butao_9.place(x=0,y=165)
butao_8 = Button(text="8",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("8"))
butao_8.place(x=80,y=165)
butao_7 = Button(text="7",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("7"))
butao_7.place(x=160,y=165)
butao_sub = Button(text="-",width=8,bg='#Fa2',fg="#fff",height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("-"))
butao_sub.place(x=240,y=165)

butao_6 = Button(text="6",width=8,height=4,relief='raised', font="15",overrelief="ridge", command=lambda: inserir("6"))
butao_6.place(x=0,y=250)
butao_5 = Button(text="5",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("5"))
butao_5.place(x=80,y=250)
butao_4 = Button(text="4",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("4"))
butao_4.place(x=160,y=250)
butao_mul = Button(text="x",width=8,bg='#Fa2',fg="#fff",height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("*"))
butao_mul.place(x=240,y=250)

butao_3 = Button(text="3",width=8,height=4,relief='raised', font="15",overrelief="ridge", command=lambda: inserir("3"))
butao_3.place(x=0,y=335)
butao_2 = Button(text="2",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("2"))
butao_2.place(x=80,y=335)
butao_1 = Button(text="1",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("1"))
butao_1.place(x=160,y=335)
butao_mul = Button(text="+",width=8,bg='#Fa2',fg="#fff",height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("+"))
butao_mul.place(x=240,y=335)

butao_0 = Button(text="0",width=20,height=4,relief='raised', font="15",overrelief="ridge", command=lambda: inserir("0"))
butao_0.place(x=0,y=420)
butao_pon = Button(text=".",width=8,height=4,relief='raised', font="15", overrelief="ridge", command=lambda: inserir("."))
butao_pon.place(x=160,y=420)
butao_mul = Button(text="=",width=8,bg='#Fa2',fg="#fff",height=4,relief='raised', font="15", overrelief="ridge", command=calcular)
butao_mul.place(x=240,y=420)


Calculadora.mainloop()