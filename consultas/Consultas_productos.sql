SELECT * FROM Productos;

SELECT * FROM Productos
WHERE categoria = 'Electrónica';

SELECT * FROM Productos
WHERE precio > 500;

SELECT * FROM Productos
ORDER BY precio DESC;

SELECT AVG(precio) AS precio_promedio
FROM Productos;

SELECT MAX(precio) AS precio_maximo, MIN(precio) AS precio_minimo
FROM Productos;