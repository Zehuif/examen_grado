SELECT
	Equipo.nombre,
	Equipo.nacionalidad 
FROM
	Equipo,
	Jugador 
WHERE
	Jugador.id_Equipo = Equipo.id_equipo 
	AND jugador.reserva = TRUE
