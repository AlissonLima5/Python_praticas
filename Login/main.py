import tkinter
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox


#Tema do aplicativo.
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')


#Janela.
janela=customtkinter.CTk()
janela.geometry("1080x600")
janela.title('Tela de Login')
janela.iconbitmap('Login/icologin.ico')

#Funções.

def error():
    messagebox.showinfo('ERROR','A pagina está em construção, volte mais tarde!')


def botao_function():
    janela.destroy()
    janela2=customtkinter.CTk()
    janela2.geometry('1280x720')
    janela2.resizable(False,False)
    janela2.title('Bem-vindo (a):!')
    janela2.iconbitmap('Login/icologin.ico')


#Comando para a imagem.
    img2=ImageTk.PhotoImage(Image.open('Login/construction.jpg',))
    l2=customtkinter.CTkLabel(master=janela2, image=img2)
    l2.pack()


#Comando para os textos da segunda página.
    t1=customtkinter.CTkLabel(master=janela2, text="Pagina inicial", font=('Century Gothic', 20))
    t1.place(x=65,y=55)

    l1=customtkinter.CTkLabel(master=janela2, text='Pagina em construção...', font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.5, anchor='center',)

    botao3=customtkinter.CTkButton(master=janela2, width=220, text='Voltar para pagina anterior', corner_radius=6, command=error)
    botao3.place(x=540, y=540)

    janela2.mainloop()


#Comando para a imagem de fundo do login.
img1=ImageTk.PhotoImage(Image.open('Login/patterns.png',))
l1=customtkinter.CTkLabel(master=janela, image=img1)
l1.pack()
#------------
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor='center')

#Comandos para o login, titulo, as entradas para o usuario digitar o login e o esqueceu sua senha.
titulo=customtkinter.CTkLabel(master=frame, text="Entre na sua conta!", font=('Century Gothic', 20))
titulo.place(x=65,y=45)


entrada1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nome do usuário')
entrada1.place(x=50, y=110)

entrada2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Senha',show='*')
entrada2.place(x=50, y=165)

esqueceu=customtkinter.CTkLabel(master=frame, text="Esqueceu sua senha?", font=('Century Gothic', 12))
esqueceu.place(x=165,y=195)


#Botão com a entrada para o login.
botao1=customtkinter.CTkButton(master=frame, width=220, text='Login', corner_radius=6, command=botao_function)
botao1.place(x=50, y=240)


#Imagens para fazer o login via Google e Facebook.
img2=customtkinter.CTkImage(Image.open('Login/google.png').resize((20,20), Image.LANCZOS))
img3=customtkinter.CTkImage(Image.open('Login/facebook.png').resize((20,20), Image.LANCZOS))

#Botão do Google e Facebook
botao_google=customtkinter.CTkButton(master=frame, image=img2, text='Google', width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='white', hover_color="#A4A4A4")
botao_google.place(x=50, y=290)

botao_facebook=customtkinter.CTkButton(master=frame, image=img3, text='Facebook', width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='white', hover_color="#A4A4A4")
botao_facebook.place(x=170, y=290)

#Mainloop para rodar a janela.
janela.mainloop()
