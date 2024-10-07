# Legajo: 109140 Nombre y apellido:  Reinaldo Aramayo

from tkinter import *
from tkinter import messagebox

def obtener_usuarios_claves():
    usuarios_claves = {
        "Reinaldo": "12345",
        "Mikael": "12345",
        "Luciano": "12345",
        "Adrian": "12345",
        "Juan": "12345"
    }
    return usuarios_claves

def abrir_ventana():
    usuarios_claves = obtener_usuarios_claves()

    def enviar_datos():
        nombre = cuadro_nombre.get()
        clave = cuadro_clave.get()
        if nombre not in usuarios_claves:
            messagebox.showerror("Error", "Alguno de los datos ingresados es incorrecto.")
        elif usuarios_claves[nombre] != clave:
            messagebox.showerror("Error", "Alguno de los datos ingresados es incorrecto")
        else:
            messagebox.showinfo("Válido", "Usuario y Clave correcto")
            ventana.destroy()

    def abrir_ventana_registro():
        def registrar_usuario():
            nuevo_usuario = cuadro_nuevo_usuario.get()
            nueva_clave = cuadro_nueva_clave.get()
            if nuevo_usuario in usuarios_claves:
                messagebox.showerror("El usuario ya existe.")
            else:
                usuarios_claves[nuevo_usuario] = nueva_clave
                messagebox.showinfo( "Usuario registrado correctamente.")
                ventana_registro.destroy()

        ventana_registro = Toplevel(ventana)
        ventana_registro.title("Registro de Usuario")
        ventana_registro.geometry("300x150")
        ventana_registro.config(bg="lightblue")

        label_nuevo_usuario = Label(ventana_registro, text="Nuevo Usuario", fg="black", bg="lightblue")
        label_nuevo_usuario.pack(pady=5)

        cuadro_nuevo_usuario = Entry(ventana_registro)
        cuadro_nuevo_usuario.pack(pady=5)

        label_nueva_clave = Label(ventana_registro, text="Nueva Clave", fg="black", bg="lightblue")
        label_nueva_clave.pack(pady=5)

        cuadro_nueva_clave = Entry(ventana_registro, show="*")
        cuadro_nueva_clave.pack(pady=5)

        botondeRegistro = Button(ventana_registro, text="Registrar", command=registrar_usuario)
        botondeRegistro.pack(pady=5)

    ventana = Tk()
    ventana.title("Login Grupo 9")
    ventana.resizable(0, 0)
    ventana.geometry("300x160")
    ventana.config(bg="pink")
    #ventana.iconbitmap("IMG_Grupo_Nro.ico")

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

    botondeRegistro = Button(ventana, text="Registrar Usuario", command=abrir_ventana_registro)
    botondeRegistro.grid(row=3, column=1, padx=0, pady=5, sticky="w")
    
    ventana.mainloop()

def main():
    abrir_ventana()

main()


