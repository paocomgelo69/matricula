CREATE TABLE aluno (
 id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
 nome VARCHAR(50) NOT NULL,
 senha VARCHAR(50) NOT NULL,
 email VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE curso (
 id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
 nome VARCHAR(50) NOT NULL UNIQUE,
 materia FLOAT NOT NULL,
 hora DATE NOT NULL,
 usuario_id INT NOT NULL,
 FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);


INSERT INTO usuarios
(nome, senha, email)
VALUES
('Jorge', 'jorge123', 'Jorge@gmail.com')

INSERT INTO usuarios
(nome, senha, email)
VALUES
('Maria', 'Maria123', 'Maria@gmail.com')


INSERT INTO usuarios
(nome, senha, email)
VALUES
('Ryan'', 'Ryan123', 'Ryan@gmail.com')




DELETE FROM usuarios 
WHERE id = 1;