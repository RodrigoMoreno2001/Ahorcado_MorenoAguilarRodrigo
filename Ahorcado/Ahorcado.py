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

        imagen = tk.PhotoImage(file="res/Ahorcado.png")
        labelImagen = tk.Label(root, image=imagen)
        labelImagen.place(x=30,y=100)

        label = tk.Label(root,text="Tematica: Frutas",bg="#482b56",fg="white",font=("verdana",16))
        label.place(x=440,y=480)
        botonReset = tk.Button(root,width=10,text="Resetear",bg="#482b56",fg="white",font=("verdana",16))
        botonReset.place(x=840,y=415)
        botonVolver = tk.Button(root,width=10,text="Volver",bg="#482b56",fg="white",font=("verdana",16))
        botonVolver.place(x=840,y=465)

        root.mainloop()


