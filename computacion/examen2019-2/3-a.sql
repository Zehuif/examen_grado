SELECT
	nombre_jugador,
	MAX( conteo ) 
FROM
	( SELECT id_jugador, COUNT( * ) AS conteo FROM sancion GROUP BY id_jugador ) AS falta,
	Jugador 
WHERE
	Jugador.id_jugador = falta.id_jugador 
GROUP BY
	nombre_jugador