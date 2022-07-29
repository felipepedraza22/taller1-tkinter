from tkinter import *
from tkinter import messagebox


def sumar ():
    i=int(x.get())*0.19
    z=int(x.get())+i
    t_resultado.insert(INSERT, "Resultados:\n El valor del Iva(0.19) de este producto es "+str(i)+"$.\n El valor total del producto es "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()


ventana_principal=Tk()
ventana_principal.title("precio IVA")
ventana_principal.geometry("800x500")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="sky blue")

x=StringVar()
i=DoubleVar()
z=IntVar()

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=750, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Ejercicio IVA")
titulo.config(bg="ivory2", fg="black", font=("Arial", 26))
titulo.place(x=320,y=10)

subtitulo2= Label(frame_entrada, text="calcular el iva y precio")
subtitulo2.config(bg="ivory2", fg="black", font=("Arial", 16), anchor=CENTER)
subtitulo2.place(x=320,y=70)

logo=PhotoImage(file="ivaa.png")
etiq_logo=Label(frame_entrada,image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)


etiq_logo1=Label(frame_entrada)
etiq_logo1.config(bg="ivory2")
etiq_logo1.place(x=590,y=10)


etiq_a=Label(frame_entrada, text="Precio del Producto = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=145)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=480,y=140)

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="white", width=780, height=120)
frame_operaciones.place(x=10,y=260)

bot_salir=PhotoImage(file="cerrar.png")
bt_salir= Button(frame_operaciones, image=bot_salir, width=100, height=100, command=salir)
bt_salir.place(x=580, y=7)

bot_sumar=PhotoImage(file="mas.png")
bt_sumar= Button(frame_operaciones, image=bot_sumar, width=150, height=150, command=sumar)
bt_sumar.place(x=80, y=7)

bot_borrar=PhotoImage(file="omar.png")
bt__borr=Button(frame_operaciones, image=bot_borrar, width=100, height=100, command=borrar)
bt__borr.place(x=280 , y=7)

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="indian red", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="black", fg="white", font=("Arial", 12))
t_resultado.pack(expand=True)

ventana_principal.mainloop()