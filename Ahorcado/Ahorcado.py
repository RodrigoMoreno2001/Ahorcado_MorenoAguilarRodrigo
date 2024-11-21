import tkinter as tk

class Ahorcado:

    def iniciarPartida(self,nombreJugador):
        root = tk.Tk()
        root.geometry("1080x620")
        root.resizable(False,False)
        root.config(bg="#482b56")



        # vista
        label = tk.Label(root,text=f"Jugador: {nombreJugador}",bg="#482b56",fg="white",font=("verdana",24))
        label.place(x=30,y=55)

        ganadasLabel = tk.Label(root,text=f"Ganadas: 0",bg="#482b56",fg="white",font=("verdana",16))
        ganadasLabel.place(x=840,y=100)

        perdidasLabel = tk.Label(root,text=f"Perdidas: 0",bg="#482b56",fg="white",font=("verdana",16))
        perdidasLabel.place(x=840,y=140)

        imagen = tk.PhotoImage(file="res/Ahorcado.png")
        imagenLabel = tk.Label(root, image=imagen)
        imagenLabel.place(x=30,y=100)

        palabraLabel = tk.Label(root,text="F _ _ _ T _",bg="#482b56",fg="white",font=("verdana",20))
        palabraLabel.place(x=440,y=100)

        letrasIntroducidasLabel = tk.Label(root,text="H, M, E, A",bg="#482b56",fg="white",font=("verdana",16))
        letrasIntroducidasLabel.place(x=440,y=140)

        tematicaLabel = tk.Label(root,text="Tematica: Frutas",bg="#482b56",fg="white",font=("verdana",16))
        tematicaLabel.place(x=440,y=480)

        botonReset = tk.Button(root,width=10,text="Resetear",bg="#482b56",fg="white",font=("verdana",16))
        botonReset.place(x=840,y=415)

        botonVolver = tk.Button(root, width=10, text="Volver", bg="#482b56", fg="white", font=("verdana",16), command=lambda: self.volver(root))
        botonVolver.place(x=840,y=465)


        root.mainloop()



    def volver(self,root):
        # Importacion diferida, implementada para corregir un error de importacion circular
        from SeleccionJugador import SeleccionJugador
        root.destroy()
        SeleccionJugador().pantalla()

