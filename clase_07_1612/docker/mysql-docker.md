# Cómo instalar y configurar MySQL en Docker

x. Instalar docker

[primeros pasos](https://www.docker.com/get-started/)

1. Descargar la imagen Docker oficial de MySQL

```
$ docker pull mysql:latest
```

2. Listar las imagenes

```
$ docker images
```

3. Ejecutar y gestionar un contenedor de servidor MySQL

```
docker run --name eduit-mysql -e MYSQL_ROOT_PASSWORD=python123 -p 3306:3306 -d mysql
```

- **run:** crea un nuevo contenedor o inicia uno existente.
- **--name CONTAINER_NAME:** da un nombre al contenedor. El nombre debe ser legible y corto. En nuestro caso, el nombre es **test-mysql**.
- **-e ENV_VARIABLE=value:** la etiqueta `-e` crea una variable de entorno que será accesible dentro del contenedor. Es crucial configurar **MYSQL_ROOT_PASSWORD** para poder ejecutar comandos SQL posteriormente desde el contenedor.
- **-d:** abreviatura de _detached_. Hace que el contenedor se ejecute en segundo plano. Si se elimina esta etiqueta, el comando seguirá imprimiendo registros hasta que el contenedor se detenga.
- **image_name:** el argumento final es el nombre de la imagen a partir de la cual se construirá el contenedor. En este caso, la imagen es **mysql**.

5. Para acceder al contenedor

```
$ docker exec -it container_name bash
```

6. entrar en mysql

mysql -u root -p (python123)

7. Ver las db

show databases;

8. Crear una DB

create database <db_name>;

9. Seleccionar la db

use <db_name>

10. Ver las tablas

show tables;

11. Crear una tabla

CREATE TABLE alumnos (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(50) NOT NULL,
edad INT,
email VARCHAR(100) UNIQUE
);

show tables;

12. Ingresar datos en la tabla

INSERT INTO alumnos (nombre, edad, email)
VALUES ("Pablo", 35, "pablo@test.com"),
("Ana", 28, "ana@test.com"),
("Luis", 22, "luis@test.com");

13. Listar todos los registros

select _ from alumnos;
select _ from alumnos limit 2;

14. filtrar

select nombre, edad where edad > 25;

15. Buscar "LIKE"

SELECT \* FROM alumnos WHERE nombre LIKE "P%"

16. Ordenar

SELECT \* FROM alumnos ORDER BY edad DESC;

17. Actualizar datos

UPDATE alumnos
SET edad = 40
WHERE nombre = "Pablo";

18. Borrar datos

DELETE FROM alumnos WHERE nombre = "Luis";

19 Borrar una tabla

drop table alumnos;
