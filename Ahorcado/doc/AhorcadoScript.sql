DROP DATABASE IF EXISTS Ahorcado;
CREATE DATABASE Ahorcado;
USE Ahorcado;

CREATE TABLE Usuario (
    nombre VARCHAR(100) PRIMARY KEY
);

CREATE TABLE Palabra (
	idPalabra INT AUTO_INCREMENT PRIMARY KEY,
    palabra VARCHAR(100),
    categoria VARCHAR(50) NOT NULL
);

CREATE TABLE Partida (
    idPartida INT AUTO_INCREMENT PRIMARY KEY,
    resultado boolean NOT NULL,
    nombre VARCHAR(100),
    idPalabra INT,
    FOREIGN KEY (nombre) REFERENCES Usuario(nombre) ON DELETE CASCADE,
    FOREIGN KEY (idPalabra) REFERENCES Palabra(idPalabra) ON DELETE CASCADE
);

INSERT INTO Palabra (palabra, categoria) VALUES ('manzana', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('platano', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('cereza', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('uva', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('naranja', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('procesador', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('memoria', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('servidor', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('algoritmo', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('bit', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('juan', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('ana', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('pedro', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('maria', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('maaaaaaartin', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('luis', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('pera', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('kiwi', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('melon', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('sandia', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('papaya', 'frutas');
INSERT INTO Palabra (palabra, categoria) VALUES ('compilador', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('byte', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('variable', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('bucle', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('archivo', 'conceptos informáticos');
INSERT INTO Palabra (palabra, categoria) VALUES ('carmen', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('jose', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('lucia', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('antonio', 'nombres de personas');
INSERT INTO Palabra (palabra, categoria) VALUES ('paula', 'nombres de personas');


INSERT INTO Usuario (nombre) VALUES ('JuanPerez');
INSERT INTO Usuario (nombre) VALUES ('AnaLopez');
INSERT INTO Usuario (nombre) VALUES ('PedroSanchez');
INSERT INTO Usuario (nombre) VALUES ('MariaGarcia');
INSERT INTO Usuario (nombre) VALUES ('LuisMartinez');

INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (1, 'JuanPerez', 1);
INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (0, 'AnaLopez', 4);
INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (1, 'PedroSanchez', 6);
INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (1, 'MariaGarcia', 9);
INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (0, 'LuisMartinez', 10);
INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (0, 'LuisMartinez', 10);
INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (1, 'LuisMartinez', 10);
INSERT INTO Partida (resultado, nombre, idPalabra) VALUES (1, 'LuisMartinez', 10);



