DROP TABLE producto;
CREATE TABLE producto(
    id_producto NUMBER(8) PRIMARY KEY,
    titulo VARCHAR2(100) NOT NULL,
    descripcion VARCHAR2(100) NOT NULL,
    stock NUMBER(8) NOT NULL,
    precio NUMBER(10, 2) NOT NULL,
    tipo VARCHAR2(30)
);

INSERT INTO producto VALUES(1,'Cemento Polpaico','Material de construcción para obras', 100, 4350, 'Materiales');
INSERT INTO producto VALUES(2,'Destornillador punta paleta','Herramienta manual para trabajos eléctricos', 50, 4990, 'Herramientas');
INSERT INTO producto VALUES(3,'Plancha OSB 11mm','Tablero OSB para estructuras y revestimientos', 30, 19670, 'Madera');
INSERT INTO producto VALUES(4,'Yeso 25kg','Material para terminaciones interiores', 80, 8990, 'Materiales');
INSERT INTO producto VALUES(5,'Destornillador Electrico','Herramienta eléctrica profesional', 25, 80990, 'Herramientas');
INSERT INTO producto VALUES(6,'Pintura Multi-superficies','Pintura para interior y exterior', 40, 124990, 'Pinturas');
INSERT INTO producto VALUES(7,'Plancha Volcanita 10 mm','Panel yeso cartón para cielos y tabiques', 60, 6590, 'Materiales');
INSERT INTO producto VALUES(8,'Escalera multipropósito','Escalera extensible aluminio 3.5m', 15, 74990, 'Herramientas');
INSERT INTO producto VALUES(9,'Yeso 5kg','Yeso para reparaciones menores', 120, 2590, 'Materiales');
INSERT INTO producto VALUES(10,'Yeso 1kg','Yeso para pequeñas reparaciones', 200, 690, 'Materiales');

COMMIT;