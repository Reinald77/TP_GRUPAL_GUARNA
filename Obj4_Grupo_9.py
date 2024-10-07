# Legajo: 109140 Nombre y apellido:  Reinaldo Aramayo

from tkinter import *
from tkinter import messagebox

def obtener_usuarios_claves():
    usuarios_claves = {
        "Reinaldo": "12345",
        "Mikael": "12345",
        "Luciano": "12345",
        "Adrian": "12345",
        "Juan" : "12345"
    }
    return usuarios_claves

def abrir_ventana():
    def enviar_datos():
        nombre = cuadro_nombre.get()
        clave = cuadro_clave.get()
        usuarios_claves = obtener_usuarios_claves()
        if not nombre in usuarios_claves:
            messagebox.showerror("Error", "Alguno de los datos ingresados es incorrecto.")
        elif not usuarios_claves[nombre] == clave:
            messagebox.showerror("Error", "Alguno de los datos ingresados es incorrecto")
        else:
            messagebox.showinfo("Valido","Usuario y Clave correcto")
            ventana.destroy()
        
    ventana = Tk()
    ventana.title("Login Grupo 9")
    ventana.resizable(0, 0)
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
    
    botondeEnvio = Button(ventana, text="Enviar", command=enviar_datos)
    botondeEnvio.grid(row=2, column=1, padx=0, pady=10, sticky="w")
    
    ventana.mainloop()

def main():
    abrir_ventana()

main()


