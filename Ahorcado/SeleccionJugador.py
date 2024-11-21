import tkinter as tk
from Ahorcado import Ahorcado
from BBDD import Conexion
class SeleccionJugador:

    def pantalla(self):
        root = tk.Tk()
        root.geometry("500x300")
        root.config(bg="#482b56")
        labelNombre = tk.Label(text="Nombre del jugador:",font=("Verdana", 16),bg="#482b56",foreground="white")
        labelNombre.pack(fill="x",pady=(50,10))
        entrada = tk.Entry( width=20,font=("Verdana", 16),bg="#dddddd")
        entrada.pack(pady="20")
        boton = tk.Button( width=10,text="Jugar!",font=("Verdana", 16), command=lambda:self.iniciarJuego(entrada.get(),root))
        boton.pack(pady="20")
        root.mainloop()

    def manejarUsuario(self,nombreJugador):
        db = Conexion()
        if not db.UsuarioExiste(nombreJugador):
            db.crearUsuario(nombreJugador)

    def iniciarJuego(self,nombreJugador,root):
        self.manejarUsuario(nombreJugador)
        root.destroy()
        ahorcado=Ahorcado(nombreJugador)
        ahorcado.iniciarVista()
