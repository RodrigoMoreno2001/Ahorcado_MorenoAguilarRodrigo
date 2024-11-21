from contextlib import nullcontext
import random

import mysql.connector
class Conexion:

    def conn(self):
      conn = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          port="3306",
          database="Ahorcado"
      )
      return conn

    def crearUsuario(self,nombreUsuario):
      conexion = None
      cursor = None
      try:
          conexion=self.conn()
          cursor = conexion.cursor()
          cursor.execute("INSERT INTO USUARIO (nombre) VALUES (%s)",(nombreUsuario,))
          conexion.commit()
      except Exception as e:
          print(f"ERROR: {e}")
      finally:
          if cursor:
              cursor.close()
          if conexion:
              conexion.close()

    def UsuarioExiste(self,nombreUsuario):

        conexion=None
        cursor=None
        try:
            conexion=self.conn()
            cursor = conexion.cursor()
            cursor.execute("SELECT nombre FROM Usuario WHERE nombre=%s",(nombreUsuario,))

            return len(cursor.fetchall())>0

        except Exception as e:
          print(f"ERROR: {e}")

        finally:
          if cursor:
            cursor.close()
          if conexion:
            conexion.close()

    def obtenerPalabra(self):
        conexion=None
        cursor=None
        try:
            conexion=self.conn()
            cursor=conexion.cursor()
            cursor.execute("SELECT count(palabra) FROM Palabra")
            palabrasTotales = cursor.fetchone()[0]
            cursor.execute("SELECT palabra,categoria,idPalabra FROM Palabra WHERE idPalabra=(%s)",(random.randint(1, palabrasTotales),))
            return cursor.fetchone()
        except Exception as e:
          print(f"ERROR: {e}")
        finally:
          if cursor:
            cursor.close()
          if conexion:
             conexion.close()

    def obtenerQuery(self,sentencia,lista):
        conexion=None
        cursor=None
        try:
            conexion=self.conn()
            cursor=conexion.cursor()
            cursor.execute(sentencia,lista)
            return cursor.fetchone()
        except Exception as e:
          print(f"ERROR: {e}")
        finally:
          if cursor:
            cursor.close()
          if conexion:
              conexion.close()

    def usuarioScore(self, resultado, nombreJugador):
        return self.obtenerQuery("SELECT count(Partida.resultado) FROM usuario INNER JOIN Partida ON Partida.nombre=usuario.nombre WHERE usuario.nombre=(%s) AND Partida.resultado=(%s)", (nombreJugador, resultado))[0]

    def insertarPartida(self,resultado,nombre,idPalabra):
        conexion = None
        cursor = None
        try:
            conexion = self.conn()
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (%s,%s,%s)", (resultado,nombre,idPalabra))
            conexion.commit()
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()