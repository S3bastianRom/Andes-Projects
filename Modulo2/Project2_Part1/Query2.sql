--Queries to filter and joins data
--With this query we intend to know which dogs and caretakers are in the designated place
WITH perro_cuidado AS (
	SELECT
		p.id_guarderia AS id_guarderia ,
		p.nombre AS nombre_perro,
        p.raza AS raza_perro,
        c.nombre AS nombre_cuidador
    FROM tablas.perro as p
    INNER JOIN tablas.cuidadores c
    ON p.id_cuidador = c.id)

SELECT
	g.nombre,
    pc.nombre_cuidador,
    pc.nombre_perro,
    pc.raza_perro
FROM perro_cuidado pc
INNER JOIN guarderias g
ON pc.id_guarderia = g.id>
WHERE g.nombre = 'La favorita'