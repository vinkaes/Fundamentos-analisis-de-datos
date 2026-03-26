

--ESTE ES UN COMPILADO DE LA QUERY, NO EJECUTAR TODO DE FORMA SIMULTÁNEA, SOLO POR SECCIONES.


/*------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                           Lección 2: Consultas a una sola tabla
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/


--Creación tabla Clientes
CREATE TABLE IF NOT EXISTS Clientes (
id_cliente TEXT PRIMARY KEY,
nombre TEXT NOT NULL,
apellido_paterno TEXT NOT NULL,
apellido_materno TEXT,
fecha_nacimiento DATE NOT NULL,
genero TEXT,
correo_cliente TEXT,
ciudad TEXT,
fecha_registro DATE NOT NULL);


--Ingreso de datos a tabla Clientes
INSERT INTO Clientes(id_cliente, nombre, apellido_paterno, apellido_materno, fecha_nacimiento, genero, correo_cliente, ciudad, fecha_registro) 
VALUES ("CLTE_1","Emma","Pérez","Hernández","02/12/1981","F","cliente_1@gmail.com","Santiago","01/01/2026"),
("CLTE_2","Thiago","Sepúlveda","Palacios","24/11/1988","M","cliente_2@gmail.com","Santiago","01/01/2026"),
("CLTE_3","Gaspar","Contreras","Palacios","10/06/1960","M","cliente_3@gmail.com","Santiago","01/01/2026"),
("CLTE_4","Aurora","Martínez","Pérez","10/05/1962","F","cliente_4@gmail.com","Iquique","01/01/2026"),
("CLTE_5","Isidora","Contreras","Rojas","05/10/2024","F","cliente_5@gmail.com","Santiago","01/01/2026"),
("CLTE_6","Josefa","Martínez","Rodríguez","26/01/2019","F","cliente_6@gmail.com","Santiago","01/01/2026"),
("CLTE_7","Gaspar","Silva","Silva","12/05/1993","M","cliente_7@gmail.com","Valparaíso","01/01/2026"),
("CLTE_8","Isabella","Rodríguez","Arias","10/02/1991","F","cliente_8@gmail.com","Valdivia","01/01/2026"),
("CLTE_9","Isabella","Muñoz","Rojas","06/07/1977","F","cliente_9@gmail.com","Santiago","01/01/2026"),
("CLTE_10","Emma","González","González","25/02/1977","F","cliente_10@gmail.com","Santiago","01/01/2026")
;

--Verificación tabla
SELECT * FROM Clientes;

--Filtro por ciudad
SELECT* FROM Clientes WHERE ciudad="Santiago";

--Filtro por nombre
SELECT* FROM Clientes WHERE nombre="Isabella";




/*------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                           Lección 3: Consultas a tablas relacionadas
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/




--Creación tabla Productos
CREATE TABLE IF NOT EXISTS Productos (
id_producto INTEGER PRIMARY KEY,
nombre_producto TEXT NOT NULL, 
categoria_producto TEXT,
marca TEXT,
precio_unitario INTEGER NOT NULL,
fecha_ingreso DATE NOT NULL)
;

--Ingreso de datos a tabla Productos
INSERT INTO  Productos (id_producto, nombre_producto, categoria_producto, marca, precio_unitario, fecha_ingreso) 
VALUES ("1000","Smartphone","Tecnología","Marca D","883810","01/01/2026"),
("1001","Parlante","Tecnología","Marca B","196820","01/01/2026"),
("1002","Audífonos","Tecnología","Marca B","286083","01/01/2026"),
("1003","Notebook","Tecnología","Marca A","703354","01/01/2026"),
("1004","Tablet","Tecnología","Marca B","848195","01/01/2026"),
("1005","Smart TV","Tecnología","Marca A","857761","01/01/2026"),
("1006","Smartwatch","Tecnología","Marca A","410463","01/01/2026"),
("1007","Consola","Tecnología","Marca B","888892","01/01/2026"),
("1008","Anillo inteligente","Tecnología","Marca D","852419","01/01/2026"),
("1009","Lente inteligente","Tecnología","Marca D","936279","01/01/2026"),
("1010","Aspiradora robot","ElectroHogar","Marca D","787487","01/01/2026"),
("1011","Lavavajillas","ElectroHogar","Marca D","672298","01/01/2026"),
("1012","Lavadora","ElectroHogar","Marca D","584880","01/01/2026"),
("1013","Microondas","ElectroHogar","Marca B","378560","01/01/2026"),
("1014","Lavadora-Secadora","ElectroHogar","Marca B","940732","01/01/2026"),
("1015","Refrigerador","ElectroHogar","Marca C","973927","01/01/2026"),
("1016","Freidora","ElectroHogar","Marca D","291082","01/01/2026"),
("1017","Horno eléctico","ElectroHogar","Marca B","312310","01/01/2026"),
("1018","Aire Acondicionado Portatil","ElectroHogar","Marca C","490758","01/01/2026"),
("1019","Robot de Cocina","ElectroHogar","Marca D","453940","01/01/2026");

--Verificación tabla
SELECT * FROM Productos;


--Creación tabla Ventas
CREATE TABLE IF NOT EXISTS Ventas (
id_venta INTEGER PRIMARY KEY,
id_cliente TEXT NOT NULL,
id_producto INTEGER NOT NULL,
fecha_venta DATE NOT NULL,
cantidad INTEGER,
descuento_aplicado DECIMAL,
total_venta INTEGER,
canales_venta TEXT,
FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
FOREIGN KEY (id_producto) REFERENCES Productos(id_producto));


--Ingreso de datos a tabla Ventas
INSERT INTO Ventas (id_venta, id_cliente, id_producto, fecha_venta, cantidad, descuento_aplicado, total_venta, canales_venta)
VALUES ("1","CLTE_8","1000","12/03/2026","3","0.3","1856001","App"),
("2","CLTE_2","1019","17/02/2026","4","0","1815760","Página Web"),
("3","CLTE_5","1000","09/02/2026","2","0.2","1414096","Página Web"),
("4","CLTE_1","1002","11/01/2026","2","0","572166","App"),
("5","CLTE_1","1017","20/02/2026","3","0","936930","App"),
("6","CLTE_5","1009","11/02/2026","1","0","936279","App"),
("7","CLTE_3","1002","11/03/2026","2","0","572166","App"),
("8","CLTE_4","1007","10/03/2026","5","0","4444460","App"),
("9","CLTE_3","1013","13/02/2026","2","0.3","529984","Página Web"),
("10","CLTE_1","1017","01/02/2026","2","0.1","562158","App"),
("11","CLTE_1","1014","02/01/2026","1","0","940732","Página Web"),
("12","CLTE_5","1001","12/01/2026","4","0","787280","Página Web"),
("13","CLTE_6","1009","08/03/2026","2","0","1872558","Página Web"),
("14","CLTE_3","1001","11/01/2026","3","0.1","531414","App"),
("15","CLTE_9","1016","25/02/2026","4","0","1164328","Página Web"),
("16","CLTE_5","1007","20/01/2026","5","0","4444460","Página Web"),
("17","CLTE_8","1000","23/02/2026","1","0","883810","App"),
("18","CLTE_1","1008","01/02/2026","5","0","4262095","Página Web"),
("19","CLTE_5","1010","01/02/2026","4","0","3149948","Página Web"),
("20","CLTE_3","1015","07/03/2026","4","0","3895708","App")
;

--Verificación tabla
SELECT * FROM Ventas;


--Qué cliente compró qué producto y cuándo.
SELECT c.nombre, c.apellido_paterno, c.apellido_materno, p.nombre_producto, v.fecha_venta
FROM  Ventas AS v
LEFT JOIN Productos AS p ON v.id_producto=p.id_producto
LEFT JOIN Clientes AS c ON v.id_cliente=c.id_cliente;


/*------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                           Lección 4: Consultas agrupadas
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

--Usar funciones como SUM(), AVG(), COUNT() sobre la tabla de ventas
SELECT FORMAT('%,d',SUM(v.total_venta)) AS SUMA_INGRESOS, FORMAT('%,d',AVG(v.total_venta)) AS MEDIA_INGRESOS, COUNT(v.total_venta) AS VENTAS_REALIZADAS
FROM  Ventas AS v ;

--Agrupar ventas por cliente y por producto
SELECT c.nombre, c.apellido_paterno, c.apellido_materno, p.nombre_producto, FORMAT('%,d',SUM(v.total_venta)) AS MONTO_VENTA
FROM  Ventas AS v
LEFT JOIN Productos AS p ON v.id_producto=p.id_producto
LEFT JOIN Clientes AS c ON v.id_cliente=c.id_cliente
GROUP BY c.nombre, c.apellido_paterno, c.apellido_materno, p.nombre_producto;

--Calcular el total de ventas por cliente
SELECT c.nombre, c.apellido_paterno, c.apellido_materno, FORMAT('%,d',SUM(v.total_venta)) AS VENTA_CLIENTE
FROM  Ventas AS v
LEFT JOIN Clientes AS c ON v.id_cliente=c.id_cliente
GROUP BY c.nombre, c.apellido_paterno, c.apellido_materno;


/*------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                           Lección 5: Consultas anidadas
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

--Listar los clientes que hayan hecho más de una compra
--- Opción A: sin subconsulta
SELECT c.nombre, c.apellido_paterno, c.apellido_materno, COUNT(v.total_venta) AS N_COMPRAS
FROM  Ventas AS v
LEFT JOIN Clientes AS c ON v.id_cliente=c.id_cliente
GROUP BY c.nombre, c.apellido_paterno, c.apellido_materno
HAVING COUNT(v.total_venta)>1;


--- Opción B: con subconsulta
SELECT  c.nombre, c.apellido_paterno, c.apellido_materno, T1.N_COMPRAS
FROM Clientes AS c
INNER JOIN (SELECT v.id_cliente,COUNT(v.total_venta) AS N_COMPRAS
           FROM  Ventas AS v
           GROUP BY v.id_cliente
           HAVING COUNT(v.total_venta)>1) AS T1 ON c.id_cliente=T1.id_cliente;
           

--Obtener el producto más vendido utilizando una subconsulta
SELECT  p.nombre_producto, T1.TOTAL_UNIDADES_VENDIDAS
FROM Productos AS p 
INNER JOIN (SELECT v.id_producto, SUM(v.cantidad) AS TOTAL_UNIDADES_VENDIDAS
           FROM  Ventas AS v
           GROUP BY v.id_producto
           ORDER BY SUM(v.cantidad) DESC
           LIMIT 1
           ) AS T1 ON p.id_producto=T1.id_producto;
           
--Consultar el cliente que más gastó en total
SELECT  c.nombre, c.apellido_paterno, c.apellido_materno, T1.GASTO_CLIENTE
FROM Clientes AS c
INNER JOIN (SELECT v.id_cliente,FORMAT('%,d',SUM(v.total_venta)) AS GASTO_CLIENTE
           FROM  Ventas AS v
           GROUP BY v.id_cliente
           ORDER BY SUM(v.total_venta) DESC
           LIMIT 1) AS T1 ON c.id_cliente=T1.id_cliente;



/*------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                           Lección 6: Creación y manipulación de tablas
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*/

--Modificar la tabla de productos para agregar una columna stock
ALTER TABLE Productos
ADD stock INT DEFAULT 100;

--Verificación cambio

SELECT* FROM Productos;


--Actualizar el stock luego de una venta

/*Ayuda para saber cuántos productos solo tuvieron una venta
SELECT v.id_producto, v.cantidad ,count(v.cantidad)
FROM  Ventas AS v
GROUP BY v.id_producto
HAVING count(v.cantidad)=1
*/

--Se actualizará el stock para el id_producto "1008" que solo vendió 5 unidades
UPDATE Productos
SET stock = 95
WHERE id_producto= "1008";

--Verificación cambio
SELECT* FROM Productos WHERE id_producto= "1008";


--Eliminar un producto obsoleto
DELETE FROM Productos
WHERE id_producto= "1012";

--Verificación cambio

SELECT* FROM Productos WHERE id_producto= "1012";
SELECT* FROM Ventas WHERE id_producto= "1012";


