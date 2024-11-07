SHOW DATABASES;
SHOW TABLES;

/*
consultas = query
tablas = table
campo/columnas|| = field
valor de campo = fueld value
registro/filas -- = records
*/


CREATE DATABASES nombre_base_datos;
DROP DATABASE nombre_base_datos;



--CREAR TABLA
CREATE TABLE mi_base_de_datos.nombre_tabla (
    id_usuarios INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    edad INT NOT NULL CHECK (edad >= 12 AND edad <= 150),
	ciudad VARCHAR(50) DEFAULT 'mundo'
);
--ELIMINAR TABLA
DROP TABLE nombre_tabla;


--INSERTAR REGISTRO*/
INSERT INTO usuarios(nombre, apellido, edad)
VALUES
	('JAVIER', 'UCIX', 21),
	('naomi', 'UCIX', 18);


-- VER TABLA
SELECT * FROM nombre_tabla;
SELECT * FROM nombre_tabla LIMIT 5;
SELECT * FROM nombre_tabla LIMIT 5 OFFSET 10; /*del registro 11(10) al 14(15)*/
SELECT * FROM nombre_tabla WHERE edad = 20; /*TODOS LOS QUE TENGAN 20*/

SELECT id_usuarios, nombre FROM usuarios
WHERE id_usuarios > 10
ORDER BY id_usuarios DESC;

--ELIMINAR REGISTRO
DELETE FROM nombre_tabla WHERE id_usuarios = 1;


--ACTUALIZAR DATO
UPDATE nombre_tabla
SET apellido = 'NuevoApellido'
WHERE id_usuarios = 5;


--ELIMINAR COLUMNA
ALTER TABLE nombre_tabla DROP COLUMN nombre_columna;


--CAMBIAR NOMBRE COLUMNA
ALTER TABLE nombre_tabla
RENAME COLUMN nombre_columna TO nombre_columna_nuevo;


