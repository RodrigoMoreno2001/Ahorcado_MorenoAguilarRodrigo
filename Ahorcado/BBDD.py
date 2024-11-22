import random
import mysql.connector

class Conexion:
    # Conexion a la BBDD, se devuelve una conexion o un None en caso de que la conexion fallase
    def conn(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port="3306",
                database="Ahorcado"
            )
            return conn
        except mysql.connector.Error as e:
            print(f"Ha ocurrido un error al conectarse: {e}")
            return None

    # Crea un usuario en BBDD

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

            # si en la query de obtiene algún resultado se devolverá true,
            # en otro caso devolveremos false
            return len(cursor.fetchall())>0

        except Exception as e:
          print(f"ERROR: {e}")

        finally:
          if cursor:
            cursor.close()
          if conexion:
            conexion.close()
    # Este metodo busca una palabra aleatoria en mi BBDD
    # y devuelve los 3 elementos que me interesan en una lista
    # esta lista será guardada en Ahorcado.palabra
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

    # Usa la funcion count() de sql para contar los resultados
    # Según el nombre y el resultado(true=ganado, false=perdido)
    # y devuelve el número de victorias o derrotas

    def usuarioScore(self, resultado, nombreJugador):
        return self.obtenerQuery("SELECT count(Partida.resultado) FROM usuario INNER JOIN Partida ON Partida.nombre=usuario.nombre WHERE usuario.nombre=(%s) AND Partida.resultado=(%s)", (nombreJugador, resultado))[0]

    # Inserta una partida en mi BBDD, se podría haber hecho un metodo insert, pero ya está terminado :D
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