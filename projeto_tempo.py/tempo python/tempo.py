import tkinter
from tkinter import *
from tkinter import ttk
import os


#importando pillow

from PIL import Image, ImageTk


################## cores ##################
co0 = "#444466"  # Preta
co1 = "#fefeff"  # branca
co2 = "#6f9fbd"  # azul

fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"

fundo = fundo_dia

janela = Tk()
janela.title('app tempo')
janela.geometry("320x350")
janela.configure(bg=fundo)

ttk.Separator(janela,orient=HORIZONTAL).grid(row=0,columnspan=1,ipadx=157)


#criando frames

frame_top = Frame(janela, width=320, height=50, bg=co1, pady=0,padx=0)
frame_top.grid(row=1,column=0)


frame_corpo = Frame(janela, width=320, height=300, bg=fundo, pady=0,padx=0)
frame_corpo.grid(row=2,column=0)



#config frame top

E_config_top = Entry(frame_top, width=30 , justify='left', highlightthickness=1 , relief='solid')
E_config_top.place(x=15,y=10)

B_config_top =Button(frame_top, text='ver clima',bg=co1,fg=co2 , relief="raised" , font=('Arial',10))
B_config_top.place(x=230,y=10)


#config frame corpo

l_cidade = Label(frame_corpo, text="paraiba - Brazil /south america", bg=fundo, anchor="center", fg=co1, font="Arial 14 bold")
l_cidade.place(x=10,y=4)


H_cidade = Label(frame_corpo, text="29 06 2025 | 10 34 12 AM", bg=fundo, anchor="center", fg=co1, font="Arial 10")
H_cidade.place(x=10,y=50)


P_cidade = Label(frame_corpo, text="80%", bg=fundo, anchor="center", fg=co1, font="Arial 40 bold")
P_cidade.place(x=10,y=90)


PE_cidade = Label(frame_corpo, text="pressao 10:13", bg=fundo, anchor="center", fg=co1, font="Arial 10 ")
PE_cidade.place(x=10,y=180)



PE_cidade = Label(frame_corpo, text="velocidade do vento: 2.12", bg=fundo, anchor="center", fg=co1, font="Arial 10 ")
PE_cidade.place(x=10,y=220)

#imagem sol

imagem = Image.open('imagens/sun.png')
imagem = imagem.resize((130,130))
imagem = ImageTk.PhotoImage(imagem)

L_iconic = Label(frame_corpo, image=imagem , bg=fundo)
L_iconic.place(x=160,y=70)

janela.mainloop()