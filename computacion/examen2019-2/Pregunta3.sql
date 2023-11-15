-- Nombre de la persona que más sanciones (de cualquier tipo) ha recibido.

SELECT Nombre FROM Jugadores WHERE sanciones = (SELECT MAX(sanciones) FROM Jugadores);

SELECT Nombre
FROM Jugadores
WHERE sanciones = (SELECT MAX(sanciones) FROM Jugadores);


-- Fechas de juegos que no hayan tenido ningún espectador.

SELECT Fecha, Hora
FROM Partida P
WHERE P.espectador_id IS NULL;

-- Nombre y nacionalidad de los equipos que tienen jugadores de reserva

SELECT Equipo.Nombre, Equipo.Nacionalidad from Jugador, Equipo WHERE Jugador.Equipo_id = Equipo.id AND Jugador.Reserva = 1 Group by Equipo.Nombre;

SELECT Equipo.Nombre from Jugador, Equipo WHERE Jugador.Equipo_id = Equipo.id AND Jugador.Reserva = 1 Group by Equipo.Nombre;
(SELECT Equipo.Nombre from Jugador, Equipo WHERE Jugador.Equipo_id = Equipo.id AND Jugador.Reserva = 1 Group by Equipo.Nombre;)
select * from equipo where nombre = (SELECT Equipo.Nombre from Jugador, Equipo WHERE Jugador.Equipo_id = Equipo.id AND Jugador.Reserva = 1 Group by Equipo.Nombre;)

-- Número de ranking y fecha en la cual cada equoi quedó en su puesto designado en el torneo

SELECT Equipo.Nombre, Equipo.Ranking, Torneo.Fecha_Torneo FROM Equipo,

-- Duración menor, superior y promedio de las partidas jugadas.

SELECT Partida.id , Partida.Duracion FROM Partida WHERE Partida.Duracion = (SELECT MIN(Partida.Duracion) FROM Partida);
SELECT Partida.id , Partida.Duracion FROM Partida WHERE Partida.Duracion = (SELECT MAX(Partida.Duracion) FROM Partida);
SELECT Partida.id , Partida.Duracion FROM Partida WHERE Partida.Duracion = (SELECT AVG(Partida.Duracion) FROM Partida);