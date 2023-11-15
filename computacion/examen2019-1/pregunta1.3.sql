--- pregunta 1.3.a
SELECT P.nombre 
FROM Participantes P, Competencia C, Prueba PU, inscripcion I
WHERE P.id = I.participanteID AND I.tipopruebaID = PU.id AND PU.competenciaID = C.id
AND C.categoria = '40-44' AND PU.distancia = 50 AND PU.estilo = 'E' AND P.genero = 'M'
ORDER BY I.tiempo ASC
LIMIT 1;

--- pregunta 1.3.b
SELECT PR.tiempo
FROM Campeonato CA, Fase F, Competencia C, Prueba PU, Participacion PR
WHERE CA.id = F.campeonatoID AND F.id = C.faseID AND C.id = PU.competenciaID AND PU.id = PR.tipopruebaID
AND CA.nombre = 'Campeonato Absoluto' AND F.nombre = 'Final' AND PU.distancia = 100 AND PU.estilo = 'M'
ORDER BY PR.tiempo ASC
LIMIT 1;

--- pregunta 1.3.c
SELECT P.nombre
FROM Participantes P, Participacion PR, Prueba PU, ParticipantesYParticipacion PYP
WHERE P.id = PYP.participanteID AND PR.id = PYP.ParticipacionID AND PR.tipopruebaID = PU.faseI
AND PU.relevo = 1 AND P.pais = 'Chile' AND PU.sexo = Mix;

--- pregunta 1.3.d
SELECT P.nombre, P.pais
FROM Participantes P, Competencia C, Prueba PU, Inscripcion I, Campeonato CA, Fase F
WHERE P.id = I.participanteID AND I.tipopruebaID = PU.id AND PU.competenciaID = C.id AND C.faseID = F.id AND F.campeonatoID = CA.id
AND CA.nombre = 'Campeonato Absoluto' AND F.nombre = 'Final' AND P.genero = 'F' AND PU.distancia = 400 AND PU.estilo = 'L';
