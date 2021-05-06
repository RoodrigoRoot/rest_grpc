# gRPC con Django (django-grpc)

Una vez dentro de la carpeta grpc, procedemos a crear el contenedor.
Para ello seguiremos los siguientes pasos:
1. `cd grpc_django/users_grpc`
2. `docker compose up`
3. Esperamos a que se cree

una vez hecho esto, ya estará nuestro contenedor ejecutandose.


# Stress Test

`ghz -c 100 -n 1000 --insecure --proto users/users.proto --call users.User.GetUser localhost:50051`
