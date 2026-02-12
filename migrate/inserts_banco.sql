USE vibetune;

INSERT INTO `vibetune`.`genero`
(`categoria`, `icone`, `cor`)
VALUES
("Rock", "", "gray"),
("MPB", "", "orange"),
("Pop", "", "purple");

INSERT INTO `vibetune`.`musica`
(`cantor`, `duracao`, `titulo`, `imagem`, `categoria`)
VALUES
("Chico Buarque", "03:56", "Apesar de Você", "https://upload.wikimedia.org/wikipedia/pt/5/59/Chico_buarque_1978.jpg", "MPB"),
("Chico Buarque", "02:51", "João e Maria", "https://cdn.gazetasp.com.br/upload/dn_arquivo/2024/06/chico-e-nara-joao-e-maria.jpeg", "MPB");
