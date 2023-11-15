
CREATE TABLE Cliente
(
  id     INT     NOT NULL AUTO_INCREMENT,
  nombre VARCHAR NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Habitacion
(
  id     INT     NOT NULL AUTO_INCREMENT,
  nombre VARCHAR NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Reserva
(
  id            INT  NULL     AUTO_INCREMENT,
  id_habitacion INT  NOT NULL,
  id_cliente    INT  NOT NULL,
  fecha_fin     DATE NULL    ,
  fecha_inicio  DATE NULL    ,
  PRIMARY KEY (id)
);

ALTER TABLE Reserva
  ADD CONSTRAINT FK_Habitacion_TO_Reserva
    FOREIGN KEY (id_habitacion)
    REFERENCES Habitacion (id);

ALTER TABLE Reserva
  ADD CONSTRAINT FK_Cliente_TO_Reserva
    FOREIGN KEY (id_cliente)
    REFERENCES Cliente (id);
