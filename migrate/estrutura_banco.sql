CREATE DATABASE IF NOT EXISTS vibetune;
USE vibetune;

CREATE TABLE IF NOT EXISTS genero (
 categoria VARCHAR(30) NOT NULL PRIMARY KEY,
 icone VARCHAR(100),
 cor CHAR(10)
);

CREATE TABLE IF NOT EXISTS musica (
 codigo_musica INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
 cantor VARCHAR(50),
 duracao TIME,
 titulo VARCHAR(100),
 imagem VARCHAR(300),
 categoria VARCHAR(30),
 CONSTRAINT FK_musica_genero
 FOREIGN KEY (categoria)
 REFERENCES genero (categoria)
);