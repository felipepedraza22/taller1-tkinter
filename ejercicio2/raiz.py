from tkinter import *
from tkinter import messagebox


def sumar ():
    z=pow(int(n.get()),1/int(x.get()))
    t_resultado.insert(INSERT, "Resultados:\n La raiz del número "+n.get()+" es "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    n.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()


ventana_principal=Tk()
ventana_principal.title("Raiz")
ventana_principal.geometry("800x500")
ventana_principal.config(bg="sky blue")
ventana_principal.resizable(0,0)

x=StringVar()
n=StringVar()
z=IntVar()

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="white", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Raiz de un número ")
titulo.config(bg="ivory2", fg="black", font=("Times New Roman", 20))
titulo.place(x=240,y=10)

logo=PhotoImage(file="r.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)


etiq_logo1=Label(frame_entrada)
etiq_logo1.config(bg="ivory2")
etiq_logo1.place(x=600,y=50)

etiq_a=Label(frame_entrada, text="Valor del índice (x): = ")
etiq_a.config(bg="ivory2", fg="black", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=110)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=480,y=105)

etiq_b=Label(frame_entrada, text="Valor del número N = ")
etiq_b.config(bg="ivory2", fg="black", font=("Arial", 15), anchor=CENTER)
etiq_b.place(x=280, y=160)

entry_b=Entry(frame_entrada, width=7, textvariable=n)
entry_b.config(font=("Arial", 20), justify=CENTER)
entry_b.focus_set()
entry_b.place(x=480,y=155)

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="cornflower blue", width=780, height=120)
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
frame_resultados.config(bg="white", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="black", fg="white", font=("Courier", 12))
t_resultado.pack(expand=True)

ventana_principal.mainloop()