import customtkinter as ctk
from PIL import ImageTk,Image
from tkinter import messagebox
import webbrowser

janela = ctk.CTk()
janela.geometry('1024x768')
janela.title('PointBlank.exe')
janela.iconbitmap('Login PointBlank/pb.ico')
janela.resizable(False,False)
janela._set_appearance_mode('Dark')


#Funções

def loginin():

    if entrada_log == 'admin' and entrada_senha == 'admin':
        messagebox.showinfo('Login','Login realizado com sucesso!')
        messagebox.showinfo('PointBlank.exe','Carregando!')
        
    else:
        messagebox.showerror('PointBlank.exe', 'Conexão com o servidor interrompida. O jogo será finalizado.')
        janela.destroy()



def cadastro():
    messagebox.showinfo('Cadastro', 'Para se cadastrar basta entrar no nosso site: (pb.ongame.net) e fazer o passo a passo para o cadastro!')
    webbrowser.open('https://pb.ongame.net/')


img1 = ImageTk.PhotoImage(Image.open('Login PointBlank/Interface_loading.png'))
loading=ctk.CTkLabel(master=janela, image=img1,)
loading.pack()

frame = ctk.CTkFrame(master=loading, width=320, height=180, corner_radius=40)
frame.place(relx=0.5, rely=0.8, anchor='center')





#Texto
entrada_usuario_label = ctk.CTkLabel(master=frame, text='ID', font=('Century Gothic',17))
entrada_usuario_label.place(x=115,y=45)

entrada_senha_label = ctk.CTkLabel(master=frame, text='Senha', font=('Century Gothic',17))
entrada_senha_label.place(x=85,y=105)



#Entrada do texto
entrada_log = ctk.CTkEntry(master=frame, width=170, height=35)
entrada_log.place(x=140,y=40)

entrada_senha = ctk.CTkEntry(master=frame, width=170, height=35, show='*')
entrada_senha.place(x=140,y=100)



#Entrada para gravar o ID
entrada_id = ctk.CTkLabel(master=frame, text='Gravar ID', font=('Century Gothic',17))
entrada_id.place(x=50,y=140)



#Botão ID
botao_id = ctk.CTkButton(master=frame,text='V', width=20, height=20, corner_radius=10,compound='left', fg_color='black', hover_color='white')
botao_id.place(x=17,y=143)

#Botão cadastre-se

botao_cad = ctk.CTkButton(master=frame, text='Cadastre-se', width=10,height=10, fg_color='gray', compound='left', command=cadastro)
botao_cad.place(x=148, y=143)

#Botão login
botao_log = ctk.CTkButton(master=frame, text='Login', width=10,height=10, fg_color='gray', compound='left', command=loginin)
botao_log.place(x=250, y=143)



janela.mainloop()