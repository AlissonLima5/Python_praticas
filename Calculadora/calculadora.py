from tkinter import *
from tkinter import ttk

cor1=("#1e1f1e") #preto
cor2=("#feffff") #branco
cor3=("#099e9e") #ciano
cor4=("#ECEFF1") #branco
cor5=("#0691d1") #azul


janela = Tk()
janela.title('Calculadora.exe')
janela.geometry('235x318')
janela.resizable(False,False)
janela.iconbitmap('Calculadora/Calculator_30001.ico')
janela.config(bg=cor1)


#frame
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)




#Atribuir os valores digitados
todos_valores = " "

#Função entrar valores
def entrar_valores(valor):
    global todos_valores
    todos_valores += str(valor)
    valor_texto.set(todos_valores)
    
#Função calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

#Função Limpa tela

def limpa_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")

#Label
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)



#Linha 1

b1 = Button(frame_corpo, command= limpa_tela,text="C", width=11, height=2,bg=cor4, font=('Ivy 13 bold'), relief=RAISED,overrelief=RIDGE,)
b1.place(x=0,y=0)
b2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text="%", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b2.place(x=118,y=0)
b3 = Button(frame_corpo, command= lambda: entrar_valores('/'),text="/", width=5, height=2,bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED)
b3.place(x=177,y=0)

#Linha 2

b4 = Button(frame_corpo, command= lambda: entrar_valores('7'),text="7", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b4.place(x=0,y=52)
b4 = Button(frame_corpo, command= lambda: entrar_valores('8'),text="8", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b4.place(x=59,y=52)
b5 = Button(frame_corpo, command= lambda: entrar_valores('9'),text="9", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b5.place(x=118,y=52)
b6 = Button(frame_corpo, command= lambda: entrar_valores('*'),text="*", width=5, height=2,bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED)
b6.place(x=177,y=52)

#Linha 3

b7 = Button(frame_corpo, command= lambda: entrar_valores('4'),text="4", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b7.place(x=0,y=104)
b8 = Button(frame_corpo, command= lambda: entrar_valores('5'),text="5", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b8.place(x=59,y=104)
b9 = Button(frame_corpo, command= lambda: entrar_valores('6'),text="6", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b9.place(x=118,y=104)
b10 = Button(frame_corpo, command= lambda: entrar_valores('-'),text="-", width=5, height=2,bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED)
b10.place(x=177,y=104)

#Linha 4

b11 = Button(frame_corpo, command= lambda: entrar_valores('1'),text="1", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b11.place(x=0,y=156)
b12 = Button(frame_corpo, command= lambda: entrar_valores('2'),text="2", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b12.place(x=59,y=156)
b13 = Button(frame_corpo, command= lambda: entrar_valores('3'),text="3", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b13.place(x=118,y=156)
b14 = Button(frame_corpo, command= lambda: entrar_valores('+'),text="+", width=5, height=2,bg=cor5,fg=cor2,font=('Ivy 13 bold'), relief=RAISED)
b14.place(x=177,y=156)

#Linha 5

b15 = Button(frame_corpo, command= lambda: entrar_valores('0'),text="0", width=11, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b15.place(x=-0,y=208)
b16 = Button(frame_corpo, command= lambda: entrar_valores('.'),text=".", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b16.place(x=117,y=208)
b17 = Button(frame_corpo, command=calcular,text="=", width=5, height=2,bg=cor4,font=('Ivy 13 bold'), relief=RAISED)
b17.place(x=177,y=208)

#MainLoop
janela.mainloop()