from tkinter import *

# Legajo: 109140 Nombre y apellido: Aramayo Reinaldo
def abrir_ventana():
    ventana = Tk()
    ventana.title("Login Grupo 9")
    ventana.resizable(0,0)
    ventana.geometry("300x130")
    ventana.config(bg="pink")
    #ventana.iconbitmap("IMG_Grupo_9.ico")
    usuario_label = Label(ventana, text="Usuario Alumno", fg="black")
    usuario_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    
    cuadro_nombre = Entry(ventana)
    cuadro_nombre.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    
    clave_label = Label(ventana, text="Clave", fg="black")
    clave_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    
    cuadro_clave = Entry(ventana, show="*")
    cuadro_clave.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    ventana.mainloop()
    
def _main_():
    abrir_ventana()

_main_()
