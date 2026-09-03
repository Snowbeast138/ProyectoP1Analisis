SELECT * FROM Products;

SELECT * FROM Products
WHERE categoria = 'Electrónica';

SELECT * FROM Products
WHERE precio > 500;

SELECT * FROM Products
ORDER BY precio DESC;

SELECT AVG(precio) AS promedio_precio
FROM Products;

SELECT MAX(precio) AS precio_maximo, MIN(precio) AS precio_minimo
FROM Products;