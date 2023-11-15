CREATE DATABASE Masters;

USE Masters;

-- TABLE USER
-- all pasword wil be encrypted using SHA1
CREATE TABLE Participantes (
  id INT(11) NOT NULL,
  nombre VARCHAR(16) UNIQUE NOT NULL,
  sexo VARCHAR(60) NOT NULL,
  edad VARCHAR(100) NOT NULL,
  pais VARCHAR(20) DEFAULT 'Cliente' NOT NULL
);

ALTER TABLE users
  ADD PRIMARY KEY (id);

ALTER TABLE users
  MODIFY id INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 2;



SELECT * FROM users;

-- Tabla de Propietarios
CREATE TABLE propietario (
  rut VARCHAR(11) NOT NULL,
  nombre VARCHAR(50) NOT NULL,
  correo VARCHAR(25) NOT NULL,
  telefono VARCHAR(50) NOT NULL,
  created_at timestamp NOT NULL DEFAULT current_timestamp,
);

ALTER TABLE proveedor
  ADD PRIMARY KEY (rut);


-- Tabla de Roles
CREATE TABLE rol (
  id INT(11) NOT NULL,
  user_id INT(11),
  nombre VARCHAR(50) NOT NULL,
  created_at timestamp NOT NULL DEFAULT current_timestamp,
  CONSTRAINT fk_userR FOREIGN KEY(user_id) REFERENCES users(id)
);

ALTER TABLE rol
  ADD PRIMARY KEY (id);

ALTER TABLE rol
  MODIFY id INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 2; 

-- Tabla de Condominio o Edificio
CREATE TABLE condominio (
  id INT(11) NOT NULL,
  administrador_id INT(11) NOT NULL,
  nombre VARCHAR(50) NOT NULL,
  ubicacion VARCHAR(50) NOT NULL,
  numero INT(11) NOT NULL,
  tipo VARCHAR(50) NOT NULL,
  created_at timestamp NOT NULL DEFAULT current_timestamp,
  CONSTRAINT fk_Admin FOREIGN KEY(administrador_id) REFERENCES users(id),
);

ALTER TABLE servicios
  ADD PRIMARY KEY (id);

ALTER TABLE servicios
  MODIFY id INT(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT = 2; 

-- Tabla de Unidad
CREATE TABLE unidad (
  numero INT(11) NOT NULL,
  condominio_id INT(11) NOT NULL,
  Pro_rut VARCHAR(11) NOT NULL,
  prerateo FLOAT(8) NOT NULL,   
  created_at timestamp NOT NULL DEFAULT current_timestamp,
  CONSTRAINT fk_Condominio FOREIGN KEY(condominio_id) REFERENCES condominio(id),
  CONSTRAINT fk_Rut FOREIGN KEY(Pro_rut) REFERENCES propietario(rut),
);

ALTER TABLE servicios
  ADD PRIMARY KEY (numero);
