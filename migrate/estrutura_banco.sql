CREATE TABLE genero (
 categoria VARCHAR(30) NOT NULL,
 icone VARCHAR(100),
 cor CHAR(10)
);

ALTER TABLE genero ADD CONSTRAINT PK_genero PRIMARY KEY (categoria);


CREATE TABLE musica (
 codigo_musica CHAR(10) NOT NULL,
 cantor VARCHAR(50),
 duracao TIME(10),
 titulo VARCHAR(100),
 imagem VARCHAR(300),
 categoria VARCHAR(30)
);

ALTER TABLE musica ADD CONSTRAINT PK_musica PRIMARY KEY (codigo_musica);


ALTER TABLE musica ADD CONSTRAINT FK_musica_0 FOREIGN KEY (categoria) REFERENCES genero (categoria);


