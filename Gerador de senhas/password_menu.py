import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox
import string
from random import random, choice
import pyperclip
import webbrowser


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

#janela
janela = customtkinter.CTk()
janela.geometry('750x500')
janela.resizable(False, False)
janela.title('Gerador de senha')
janela.iconbitmap('Gerador de senhas/passwordicon.ico')

    
def gerar_senha():

    valores = string.ascii_letters + string.digits + string.punctuation
    caracteres = 14
    senha = ""

    for i in range (caracteres):
        senha += choice(valores)
    
    exibir_senha.delete(0, "end")  # Apaga o texto anterior
    exibir_senha.insert(0, senha)  # Insere a nova senha gerada

    print(senha)
    return

def copiar_senha():
    senha = exibir_senha.get()  # Obtém o texto da caixa de entrada
    pyperclip.copy(senha)        # Copia para a área de transferência
    messagebox.showinfo('Senha copiada', 'A senha foi copiada para aréa de transferência!')


def site_senha():
    webbrowser.open('https://password.kaspersky.com/pt/')


def descricao():
    messagebox.showinfo('Descrição', 'Este programa foi criado para gerar senhas mais seguras, ideais para sites como Gmail, Hotmail e outros. Você pode usar a senha gerada ou personalizá-la conforme suas preferências, mantendo sua força original. Dessa forma, sua conta estará mais protegida e segura contra possíveis invasões. Não se esqueça de testar a senha no site de verificação!')


def sair_programa():
    messagebox.showinfo('Gerador de senha', 'Obrigado por usar o gerador de senha!')
    janela.destroy()


#Imagens
img = ImageTk.PhotoImage(Image.open('Gerador de senhas/passwordwallpaper2.jpg'))
l1 = customtkinter.CTkLabel(master=janela, image=img)
l1.image = img  # Mantenha a referência da imagem para evitar que o Python descarte
l1.pack()

#Frame 
frame = customtkinter.CTkFrame(master=l1, width=480,height=340, corner_radius=22, fg_color="transparent")
frame.place(relx=0.5, rely=0.5, anchor='center')

#Titulo do frame
titulo=customtkinter.CTkLabel(master=frame, text='Gerador de senhas!', font=('Century Gothic', 20))
titulo.place(x=243,y=40, anchor='center')


#Exibir senha
exibir_senha = customtkinter.CTkEntry(master=frame, font=('Century Gothic', 19), width=190)
exibir_senha.place(relx=0.5, rely=0.3, anchor='center')


#Botão para gerar a senha
botao_gerador = customtkinter.CTkButton(master=frame, width=240, text='Gerar senha aleatoria', corner_radius=10, command=gerar_senha)
botao_gerador.place(relx=0.5, rely=0.5, anchor='center')

#Botão para copiar a senha
botao_copiar = customtkinter.CTkButton(master=frame, width=240, text='Copiar senha', corner_radius=10, command=copiar_senha)
botao_copiar.place(relx= 0.5, rely= 0.6, anchor='center')

#Botão para entrar no site de verificação
botao_site = customtkinter.CTkButton(master=frame, width=240, text='Site para verificar a senha', corner_radius=10, command=site_senha)
botao_site.place(relx= 0.5, rely= 0.7, anchor='center')


#Botão de descrição do programa
botao_descricao = customtkinter.CTkButton(master=frame, width=140, text='Descrição', corner_radius=10, command=descricao)
botao_descricao.place(relx= 0.2, rely= 0.9, anchor='center')

#Botão para sair do programa
botao_sair = customtkinter.CTkButton(master=frame, width=140, text='Sair', corner_radius=10, command=sair_programa)
botao_sair.place(relx= 0.8, rely= 0.9, anchor='center')

#loop
janela.mainloop()