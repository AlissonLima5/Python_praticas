import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

janela=customtkinter.CTk()
janela.geometry("1080x600")
janela.title('Tela de Login')
janela.iconbitmap('Login/icologin.ico')


def botao_function():
    janela.destroy()
    janela2=customtkinter.CTk()
    janela2.geometry('1280x720')
    janela2.title('Bem-vindo (a):!')
    janela2.iconbitmap('Login/icologin.ico')
    t1=customtkinter.CTkLabel(master=janela2, text="Pagina inicial", font=('Century Gothic', 20))
    t1.place(x=65,y=55)
    l1=customtkinter.CTkLabel(master=janela2, text='Pagina em construção...', font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.5, anchor='center')
    janela2.mainloop()


img1=ImageTk.PhotoImage(Image.open('Login/patterns.png'))
l1=customtkinter.CTkLabel(master=janela, image=img1)
l1.pack()

frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor='center')


titulo=customtkinter.CTkLabel(master=frame, text="Entre na sua conta!", font=('Century Gothic', 20))
titulo.place(x=65,y=45)


entrada1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nome do usuário')
entrada1.place(x=50, y=110)

entrada2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Senha',show='*')
entrada2.place(x=50, y=165)

esqueceu=customtkinter.CTkLabel(master=frame, text="Esqueceu sua senha?", font=('Century Gothic', 12))
esqueceu.place(x=165,y=195)

botao1=customtkinter.CTkButton(master=frame, width=220, text='Login', corner_radius=6, command=botao_function)
botao1.place(x=50, y=240)

img2=customtkinter.CTkImage(Image.open('Login/google.png').resize((20,20), Image.LANCZOS))
img3=customtkinter.CTkImage(Image.open('Login/facebook.png').resize((20,20), Image.LANCZOS))

botao_google=customtkinter.CTkButton(master=frame, image=img2, text='Google', width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='white', hover_color="#A4A4A4")
botao_google.place(x=50, y=290)

botao_facebook=customtkinter.CTkButton(master=frame, image=img3, text='Facebook', width=100, height=20, corner_radius=6, compound='left', text_color='Black', fg_color='white', hover_color="#A4A4A4")
botao_facebook.place(x=170, y=290)

janela.mainloop()