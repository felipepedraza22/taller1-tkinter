

from tkinter import *
from tkinter import messagebox

#---------------------
# Funciones de la App
#---------------------

def sumar ():
    z=int(x.get())*(int(x.get())+1)/2
    t_resultado.insert(INSERT, "Resultados:\n La suma de los primeros "+x.get()+" enteros positivos es : "+str(z)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos serán borrados...")
    x.set("")
    t_resultado.delete("1.0", "end")

def salir():
    messagebox.showinfo("Suma 1.0", "La App se cerrará...")
    ventana_principal.destroy()


ventana_principal=Tk()


ventana_principal.title("Numeros enteros")


ventana_principal.geometry("800x500")

ventana_principal.resizable(0,0)


ventana_principal.config(bg="snow")

x=StringVar()
z=IntVar()



frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=780, height=240)
frame_entrada.place(x=10,y=10)

titulo= Label(frame_entrada, text="Iva y Precio Final")
titulo.config(bg="ivory2", fg="black", font=("Arial", 20))
titulo.place(x=240,y=10)

subtitulo2= Label(frame_entrada, text="Determinar la suma de los primeros \n N enteros positivos usando la fórmula.")
subtitulo2.config(bg="ivory2", fg="black", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=240,y=70)


etiq_logo=Label(frame_entrada)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)

etiq_a=Label(frame_entrada, text="Número N = ")
etiq_a.config(bg="ivory2", fg="black", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=280, y=145)

entry_a=Entry(frame_entrada, width=7, textvariable=x)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=480,y=140)


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
frame_resultados.config(bg="indian red", width=780, height=100)
frame_resultados.place(x=10,y=390)

t_resultado=Text(frame_resultados, width=77, height=5)
t_resultado.config(bg="black", fg="white", font=("Courier", 12))
t_resultado.pack(expand=True)


ventana_principal.mainloop()