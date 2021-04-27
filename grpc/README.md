# gRPC con Python

Una vez dentro de la carpeta grpc, procedemos a crear el contenedor.
Para ello seguiremos los siguientes pasos:

1. `docker build -t python-grpc .`
2. Esperamos a que se cree
3. `docker run -p 50050:50050 python-grpc`

una vez hecho esto, ya estará nuestro contenedor ejecutandose.
