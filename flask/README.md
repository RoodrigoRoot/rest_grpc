# gRPC con Flask

Una vez dentro de la carpeta grpc, procedemos a crear el contenedor.

Para ello seguiremos los siguientes pasos:

1. `cd flask`
2. `docker build -t flask-grpc .`
3. Esperamos a que se cree
4. `docker run -p 50049:50049 flask-grpc`

una vez hecho esto, ya estará nuestro contenedor ejecutandose.

# Stress Test

`ghz -c 100 -n 1000 --insecure --proto users.proto --call users.User.GetUser localhost:50050`

