SELECT
	Equipo.nombre,
	Resultados.Ranking,
	Resultados.fecha 
FROM
	Equipo,
	Resultados 
WHERE
	Equipo.id_equipo = Resultados.id_equipo 
	AND id_torneo = "1" #Se asume que se quiere saber para un torneo en específico
	
ORDER BY
	Resultados.Ranking DESC
