# Pruebas gRPC con Python

## Las pruebas fueron realizadas en:

- Python
- Django (django-grpc)
- Flask

Cada uno de los proyectos está hecho con **Docker**, por lo cual se podrá ejecutar sin ningún problema.

Los puertos que se necesitan para poder ejecutar cada proyecto son los siguientes:

- 50051 (django-grpc)
- 50050 (Python)
- 50049 (Flask)

## Instalación
En cada proyectos está un README, en el cual podrán ver las indicaciones para poder crear o ejecutar los contenedores.
Una vez que se haya hecho la instalación, se debe entrar dentro del contenedor:

`docker exec -ti <nombre_del_contenedor> bash`

Una vez dentro, solo ejecutaremos el archivo llamado **client.py**
