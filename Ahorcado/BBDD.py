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

  def insert(self,sentencia, lista):
    conexion=None
    cursor=None
    try:
      conexion = self.conn()
      cursor = conexion.cursor()
      cursor.execute(sentencia, lista)
      conexion.commit()
      print("Insercion realizada con éxito...")
    except Exception as e:
      print(f"ERROR: {e}")
    finally:
      if cursor:
        cursor.close()
      if conexion:
        conexion.close()

  def listar(self,sentencia):
      conexion = None
      cursor = None
      try:
          conexion = self.conn()
          cursor = conexion.cursor()
          cursor.execute(sentencia)

          for e in cursor:
              print(e)

      except Exception as e:
          print(f"ERROR: {e}")
      finally:
          if cursor:
              cursor.close()
          if conexion:
              conexion.close()