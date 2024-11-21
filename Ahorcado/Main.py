from Ahorcado import Ahorcado
from BBDD import Conexion
from SeleccionJugador import SeleccionJugador

"""
TODO

Ventana de seleccion de jugador:
    -comprobar si el player existen en db, si no existe se crea
    -No permitir valores vacíos
    
Ventana de juego:
    -Hacer imagen cambiante
"""

def main():

    SeleccionJugador().pantalla()


   # Ahorcado().iniciarPartida("nombreJugador")

if __name__ == '__main__':
    main()