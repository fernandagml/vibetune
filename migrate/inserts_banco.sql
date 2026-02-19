USE vibetune;

INSERT INTO `vibetune`.`genero`
(`categoria`, `icone`, `cor`)
VALUES
("Trap", "", "gray"),
("MPB", "", "orange"),
("Gospel", "", "aquamarine"),
("Samba", "", "yellow"),
("Hip Hop", "", "purple"),
("Sertanejo", "", "brown");

INSERT INTO `vibetune`.`musica`
(`cantor`, `duracao`, `titulo`, `imagem`, `categoria`)
VALUES
("Chico Buarque", "00:03:56", "Apesar de Você", "https://upload.wikimedia.org/wikipedia/pt/5/59/Chico_buarque_1978.jpg", "MPB"),
("Chico Buarque", "00:02:51", "João e Maria", "https://cdn.gazetasp.com.br/upload/dn_arquivo/2024/06/chico-e-nara-joao-e-maria.jpeg", "MPB"),
("Legião Urbana", "00:05:02", "Tempo Perdido", "https://cdn-images.dzcdn.net/images/cover/b4738becedbed0481ac71cee50b18d6b/1900x1900-000000-80-0-0.jpg", "MPB"),
("Grupo Fundo de Quintal", "00:03:29", "O Show Tem Que Continuar", "https://is1-ssl.mzstatic.com/image/thumb/Music6/v4/47/c3/f2/47c3f2d9-3501-807c-39d2-78a4c42acbf7/7891430055271.jpg/600x600bf-60.jpg", "Samba"),
("Rita Lee", "00:04:55", "Mania de Você", "https://cdn-images.dzcdn.net/images/cover/5b75ee72667f22553972afa40a4f1547/0x1900-000000-80-0-0.jpg", "MPB"),
("Gal Costa", "00:04:02", "Palavras No Corpo", "https://akamai.sscdn.co/uploadfile/letras/albuns_high/163490_20250427080448.jpg", "MPB"),
("Racionais MC's", "00:06:51", "Negro Drama", "https://upload.wikimedia.org/wikipedia/pt/3/36/Sobrevivendo_no_Inferno.jpg", "Hip Hop"),
("Matuê", "00:04:24", "Anos Luz", "https://cdn-images.dzcdn.net/images/cover/1e0e4b9cb9d3cdd462ea03b0a5bc22ad/0x1900-000000-80-0-0.jpg", "Trap"),
("Marisa Monte", "00:02:53", "Depois", "https://i1.sndcdn.com/artworks-000052634468-e4ehl1-t500x500.jpg", "MPB"),
("Racionais MC's", "00:05:03", "Vida Loka, Pt. 1", "https://upload.wikimedia.org/wikipedia/pt/3/36/Sobrevivendo_no_Inferno.jpg", "Hip Hop"),
("Marina Lima", "00:05:05", "Não Sei Dançar", "https://i.ytimg.com/vi/Jjq0RWa_sXo/maxresdefault.jpg", "MPB"),
("Ritchie", "00:04:41", "Menina Veneno", "https://igormiranda.com.br/wp-content/uploads/2024/08/ritchie-menina-veneno-1983-frente-lp.jpg", "MPB");