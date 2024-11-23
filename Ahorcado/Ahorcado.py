import tkinter as tk
from tkinter import messagebox
from BBDD import Conexion

class Ahorcado:

    def __init__(self,nombreJugador):
        self.nombreJugador=nombreJugador
        self.db=Conexion()
        self.intentos = 0
        self.palabra = self.db.obtenerPalabra()
        self.palabraMaquina = self.palabra[0]
        self.letrasIntroducidas = []
        self.tematica = self.palabra[1]

        # Algunos elementos de la vista los he tenido que declarar a nivel de clase
        # para hacerlos accesible de una forma más cómoda...

        self.root = tk.Tk()
        self.imagen = ""
        self.ganadasLabel= tk.Label(self.root, bg="#482b56", fg="white", font=("verdana", 16))
        self.perdidasLabel=tk.Label(self.root, bg="#482b56", fg="white", font=("verdana", 16))
        self.tematicaLabel=tk.Label(self.root,bg="#482b56",fg="white",font=("verdana",16))
        self.palabraLabel= tk.Label(self.root, bg="#482b56", fg="white", font=("verdana", 20))
        self.letrasIntroducidasLabel= tk.Label(self.root, bg="#482b56", fg="white", font=("verdana", 16))
        self.imagenLabel = tk.Label(self.root, image=self.imagen)
        self.imagen = tk.PhotoImage(file=f"res/a{self.intentos}.png")

    def iniciarVista(self):
        self.root.geometry("1080x620")
        self.root.resizable(False,False)
        self.root.config(bg="#482b56")
        self.root.title("ElAhorcado")
        self.root.bind("<KeyPress>", self.key_event) # Liga un KeyListener a la ventana

        # Algunos elementos restantes de la vista y posicionamiento

        label = tk.Label(self.root,text=f"Jugador: {self.nombreJugador}",bg="#482b56",fg="white",font=("verdana",24))
        botonReset = tk.Button(self.root,width=10,text="Resetear",font=("verdana",16),command=lambda: self.reiniciarJuego())
        botonVolver = tk.Button(self.root, width=10, text="Volver",font=("verdana",16), command=lambda: self.volver(self.root))
        self.imagen = tk.PhotoImage(file="res/a0.png")

        label.place(x=30,y=55)
        self.ganadasLabel.place(x=840,y=100)
        self.perdidasLabel.place(x=840,y=140)
        self.imagenLabel.place(x=30,y=100)
        self.palabraLabel.place(x=440,y=100)
        self.letrasIntroducidasLabel.place(x=440,y=180)
        self.tematicaLabel.place(x=440,y=470)
        botonReset.place(x=840,y=415)
        botonVolver.place(x=840,y=465)

        self.actualizarVista()
        self.root.mainloop()

    # metodo listener
    def key_event(self, event):
        letra = event.char.lower()
        if letra.isalpha(): # comprueba si la key está en el alfabeto
            if letra not in self.letrasIntroducidas and self.intentos<10:
                self.letrasIntroducidas.append(letra)
                self.comprobar(letra)

    def comprobar(self,letra):
        if letra not in self.palabraMaquina:
            self.intentos+=1
            if self.intentos >= 10:
                # Si el código llega hasta aquí significa que has perdido,
                # por lo tanto se inserta una nueva partida en tu nombre con el resultado false(0)
                Conexion().insertarPartida(0, self.nombreJugador, self.palabra[2])
                self.actualizarVista()
                if messagebox.askyesno("Perdiste", f"La palabra era {self.palabraMaquina}, quieres volver a intentarlo?"):
                    self.reiniciarJuego()
            else:
                self.actualizarVista()
        else:
            # se crean 2 sets, estos sets como bien dijo Niko no contienen duplicados
            # por lo tanto si obtenemos la inserseccion entre ambos y el resultado
            # tiene la misma longitud que el set(palabraMaquina),
            # significa que el usuario ha adivinado la palabra

            set1=set(self.palabraMaquina)
            set2=set(self.letrasIntroducidas)

            if len((set1 & set2))==len(set1):
                Conexion().insertarPartida(1, self.nombreJugador, self.palabra[2])
                self.actualizarVista()
                if messagebox.askyesno("Ganaste", "Has ganado, quieres volver a jugar?"):
                    self.reiniciarJuego()
            else:
                self.actualizarVista()

    def volver(self,root):
        # Importacion diferida, implementada para corregir un error de importacion circular
        from SeleccionJugador import SeleccionJugador
        root.destroy()
        SeleccionJugador().pantalla()

    # este metodo es el encargado de manejar las vistas cambiantes de tkinter
    def actualizarVista(self):
        db=Conexion()
        self.ganadasLabel.config(text=f"Ganadas: {db.usuarioScore(1,self.nombreJugador)}")
        self.perdidasLabel.config(text=f"Perdidas: {db.usuarioScore(0, self.nombreJugador)}")

        self.tematicaLabel.config(text=f"Tematica: {self.tematica}")

        self.palabraLabel.config(text=f"{self.actualizarPalabra()}")

        introducidas=", ".join(self.letrasIntroducidas)
        self.letrasIntroducidasLabel.config(text=f"{introducidas}")

        self.imagen = tk.PhotoImage(file=f"res/a{self.intentos}.png")
        self.imagenLabel.config(image=self.imagen)

    # reinicia el juego a su estado base
    def reiniciarJuego(self):
        self.intentos = 0
        self.palabra=self.db.obtenerPalabra()
        self.palabraMaquina = self.palabra[0]
        self.letrasIntroducidas = []
        self.tematica = self.palabra[1]
        self.actualizarVista()


    def actualizarPalabra(self):
        ret=""
        # para la palabra dada por BBDD:
        # comprobamos si la letra dada en la iteracion está en el array self.letrasIntroducidas
        # si se encuentra, imprimimos la letra
        # si no, imprimimos una _ y su correspondiente espacio para que se vea bonico
        for i in range(len(self.palabraMaquina)):
            if(self.palabraMaquina[i] in self.letrasIntroducidas):
                ret+=self.palabraMaquina[i]+" "
            else:
                ret+="_ "
        return ret