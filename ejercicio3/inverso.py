from tkinter  import *

from tkinter import CENTER, INSERT, Button, Entry, Frame, Label, StringVar, messagebox

from matplotlib import image



def sumar ():
    a=int(x.get())%10
    a1=int(x.get())//10
    a2=a*1000
    b=a1%10
    b1=a1//10
    b2=b*100
    c=b1%10
    c1=b1//10
    c2=c*10

    z=a2+b2+c2+c1

    t_resultado.insert(INSERT, "Resultados:\n El número "+x.get()+" a la inversa es "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()



ventana_principal=Tk()

ventana_principal.title("inverso de un numero")

ventana_principal.geometry("800x500")


ventana_principal.resizable(0,0)

ventana_principal.config(bg="snow")


x=StringVar()
a=IntVar()
a1=IntVar()
a2=IntVar()

b=IntVar()
b1=IntVar()
b2=IntVar()

c=IntVar()
c1=IntVar()
c2=IntVar()
z=IntVar()


frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Número Inverso")
titulo.config(bg="ivory2", fg="black", font=("Times New Roman", 20))
titulo.place(x=240,y=10)

etiq_logo=Label(frame_entrada)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)

etiq_a=Label(frame_entrada, text="Número de 4 dígitos = ")
etiq_a.config(bg="ivory2", fg="black", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=120)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=490,y=115)

logo=PhotoImage(file="s.png")
etiq_logo=Label(frame_entrada,image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="sky blue", width=780, height=120)
frame_operaciones.place(x=10,y=260)


bot_sumar=PhotoImage(file="mas.png")
bt_sumar= Button(frame_operaciones, image=bot_sumar, width=105, height=105, command=sumar)
bt_sumar.place(x=116, y=7)

bot_borrar=PhotoImage(file="omar.png")
bt_borrar= Button(frame_operaciones, image=bot_borrar, width=105, height=105, command=borrar)
bt_borrar.place(x=337, y=7)

bot_salir=PhotoImage(file="cerrar.png")
bt_salir= Button(frame_operaciones, image=bot_salir, width=105, height=105, command=salir)
bt_salir.place(x=585, y=7)

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="indian red", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="black", fg="white", font=("Courier", 12))
t_resultado.pack(expand=True)


ventana_principal.mainloop()