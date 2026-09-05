CREATE DATABASE IF NOT EXISTS tienda_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE tienda_db;

DROP TABLE IF EXISTS Productos;

CREATE TABLE Productos (
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO Productos (id_producto, nombre, categoria, precio, stock) VALUES 
(1, 'Laptop Pro', 'Electrónica', 25000.00, 50),
(2, 'Smartphone X', 'Electrónica', 15000.00, 100),
(3, 'Monitor 27\"', 'Periféricos', 4500.00, 30),
(4, 'Teclado Mecánico', 'Periféricos', 1200.00, 80),
(5, 'Mouse Inalámbrico', 'Periféricos', 600.00, 120),
(6, 'Auriculares Bluetooth', 'Audio', 1800.00, 60),
(7, 'Smartwatch Series 5', 'Electrónica', 5500.00, 40),
(8, 'Tablet 10\"', 'Electrónica', 8000.00, 70),
(9, 'Cámara Web 1080p', 'Periféricos', 900.00, 50),
(10, 'Micrófono USB', 'Audio', 1500.00, 25),
(11, 'Disco Duro Externo 2TB', 'Almacenamiento', 2000.00, 90),
(12, 'Memoria RAM 16GB', 'Componentes', 1400.00, 110),
(13, 'Tarjeta Gráfica RTX 4060', 'Componentes', 8500.00, 15),
(14, 'Silla Gamer', 'Mobiliario', 3500.00, 20),
(15, 'Escritorio Ajustable', 'Mobiliario', 6000.00, 10);