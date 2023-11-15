SELECT DISTINCT
	Partido.fecha 
FROM
	Espectador_Partido,
	Partido 
WHERE
	Partido.id_partido <> Espectador_Partido.id_partido
