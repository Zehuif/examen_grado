-- Utilizo MYSQL

-- Nombre del plato que mas dinero genera


SELECT plato.nombre , SUM(plato.valor)
FROM plato pedido 
WHERE plato.id = pedido.plato_id 
GROUP BY nombre.plato
ORDER BY SUM(plato.valor) DESC
HAVING SUM(plato.valor) = (SELECT MAX(SUM(plato.vlaor)) FROM plato pedido WHERE plato.id = pedido.plato_id GROUP BY plato.nombre);



-- Ranking de los clientes mas frecuentes (de mayor a menor) en que se despliega el nombre telefono de ellos

SELECT cliente.nombre, cliente.telefono 
FROM cliente , reserva
WHERE cliente.id = reserva.cliente_id
Group BY id.cliente
ORDER BY COUNT(reserva.cliente_id) DESC;

-- Tiempo promedio de espera de los clientes por platos en el restaurante
-- Para esto utilizo una tabla de union entre plato y cocinero que se llamara preparacion que tienen las
-- FK de plato y cocinero, ademas el tiempo de preparacion del plato
-- Lo realizo de esta forma ya que asi se el tiempo especifico en preparar un plato ya que si utilizo mi tabla de
-- pedido este tiene el tiempo total de todo el pedido.

SELECT plato.nombre, AVG(preparacion.tiempo)
FROM plato, prepararacion
WHERE plato.id = preparacion.plato_id
GROUP BY plato.id
ORDER BY AVG(preparacion.tiempo) DESC; 



