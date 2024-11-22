import tkinter as tk
from Ahorcado import Ahorcado
from BBDD import Conexion
from tkinter import messagebox

class SeleccionJugador:

    def pantalla(self):
        # Vista de la pantalla de selección
        root = tk.Tk()
        root.geometry("500x300")
        root.config(bg="#482b56")
        root.title("ElAhorcado: Seleccion de Jugador")

        labelNombre = tk.Label(text="Nombre del jugador:",font=("Verdana", 16),bg="#482b56",foreground="white")
        labelNombre.pack(fill="x",pady=(50,10))

        entrada = tk.Entry( width=20,font=("Verdana", 16),bg="#dddddd")
        entrada.pack(pady="20")

        boton = tk.Button( width=10,text="Jugar!",font=("Verdana", 16), command=lambda:self.iniciarJuego(entrada.get(),root))
        boton.pack(pady="20")

        root.mainloop()

    # Este metodo busca un usuario en bbdd, si no existe, lo crea.

    def manejarUsuario(self,nombreJugador):
        db = Conexion()
        if not db.UsuarioExiste(nombreJugador):
            db.crearUsuario(nombreJugador)

    # Comprueba que el nombre no está vacío e inicia el juego en nombre de tal usuario

    def iniciarJuego(self,nombreJugador,root):

        if not nombreJugador:
            messagebox.showinfo("ERROR!","El nombre no puede estar vacío")
            return

        self.manejarUsuario(nombreJugador)

        root.destroy()

        ahorcado=Ahorcado(nombreJugador)
        ahorcado.iniciarVista()
