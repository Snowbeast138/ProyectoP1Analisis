CREATE TABLE Productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100),
    categoria VARCHAR(50),
    precio DECIMAL(10, 2),
    stock INT
);

INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (1, 'Laptop Pro', 'Electrónica', 25000.0, 50);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (2, 'Smartphone X', 'Electrónica', 15000.0, 100);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (3, 'Monitor 27"', 'Periféricos', 4500.0, 30);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (4, 'Teclado Mecánico', 'Periféricos', 1200.0, 80);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (5, 'Mouse Inalámbrico', 'Periféricos', 600.0, 120);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (6, 'Auriculares Bluetooth', 'Audio', 1800.0, 60);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (7, 'Smartwatch Series 5', 'Electrónica', 5500.0, 40);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (8, 'Tablet 10"', 'Electrónica', 8000.0, 70);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (9, 'Cámara Web 1080p', 'Periféricos', 900.0, 50);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (10, 'Micrófono USB', 'Audio', 1500.0, 25);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (11, 'Disco Duro Externo 2TB', 'Almacenamiento', 2000.0, 90);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (12, 'Memoria RAM 16GB', 'Componentes', 1400.0, 110);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (13, 'Tarjeta Gráfica RTX 4060', 'Componentes', 8500.0, 15);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (14, 'Silla Gamer', 'Mobiliario', 3500.0, 20);
INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES (15, 'Escritorio Ajustable', 'Mobiliario', 6000.0, 10);
