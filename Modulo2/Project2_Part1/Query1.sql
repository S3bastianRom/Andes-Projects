-- This query insterts dummy data into each database

INSERT INTO `TABLAS`.`guarderias` (`id`, `nombre`, `direccion`, `telefono`) VALUES
(1, 'Guarderia Sol', 'Avenida Libertad 123', '555-1234567'),
(2, 'Guarderia Luna', 'Calle 456', '555-2345678'),
(3, 'Guarderia Estrella', 'Calle del Sol 789', '555-3456789'),
(4, 'Guarderia Arco Iris', 'Avenida Central 101', '555-4567890'),

--Getting data
SELECT * FROM TABLAS.guarderias;


--Inserting data
INSERT INTO `TABLAS`.`cuidadores` (`id`, `nombre`, `telefono`, `id_guarderia`) VALUES
(1, 'Juan Perez', '555-1112233', 1),
(2, 'Ana Gomez', '555-2223344', 2),
(3, 'Pedro Rodriguez', '555-3334455', 3),
(4, 'Lucia Martinez', '555-4445566', 4),
--Getting data
SELECT * FROM TABLAS.CUIDADORES;

--Inserting data
INSERT INTO `TABLAS`.`perro` (`id`, `nombre`, `raza`, `edad`, `id_guarderia`, `id_cuidador`) VALUES
(1, 'Rex', 'Labrador', 5, 1, 1),
(2, 'Bella', 'Poodle', 3, 1, 1),
(3, 'Max', 'Beagle', 4, 2, 2),
(4, 'Rocky', 'Bulldog', 2, 2, 2),
--Getting data
SELECT * FROM TABLAS.PERRO;