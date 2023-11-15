-- Para la wea 

-- Tabla de Personajes
CREATE TABLE Personajes (
  id INT(11) NOT NULL,
  Partida_id INT(11) NOT NULL,
  Jugador_ID INT(11) NOT NULL,
  CONSTRAINT fk_Partida FOREIGN KEY(Partida_id) REFERENCES Partida(id),
  CONSTRAINT fk_Jugador FOREIGN KEY(Jugador_id) REFERENCES Jugador(id),
);

ALTER TABLE Personajes
  ADD PRIMARY KEY (id);

ALTER TABLE Personajes
  MODIFY id INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 2; 