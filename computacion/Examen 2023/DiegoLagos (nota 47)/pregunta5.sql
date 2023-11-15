-- pregunta5 - Diego Lagos - Examen de grado 2023-1

---Nombre del plato que más dinero genera

SELECT plato.nombre FROM plato as pa, comanda as co FROM platos, comanda WHERE comanda.platosID = plato.ID GROUP BY plato.nombre ORDER BY SUM(comanda.precio) DESC LIMIT 1;

---Raking de los clientes más frecuentes
SELECT cliente.nombre FROM cliente, asiste WHERE cliente.ID = asiste.clienteID GROUP BY cliente.nombre ORDER BY COUNT(asiste.clienteID) DESC;

---Tiempo promedio de espera de los clientes por platos en el restaurante
SELECT plato.nombre FROM comanda Where comanda.platosID = plato.ID GROUP BY plato.nombre ORDER BY AVG(comanda.emiteDate - comnda.cierraDate) DESC;