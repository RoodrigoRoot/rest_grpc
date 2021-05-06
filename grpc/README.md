# gRPC con Python

Una vez dentro de la carpeta grpc, procedemos a crear el contenedor.
Para ello seguiremos los siguientes pasos:

1. `docker build -t python-grpc .`
2. Esperamos a que se cree
3. `docker run -p 50050:50050 python-grpc`

una vez hecho esto, ya estará nuestro contenedor ejecutandose.

# Stress Test

`ghz  -c 100 -n 1000 --insecure  --proto trading.proto -d '{"company":"74104cea-e9b3-422b-980f-a13fb4ff8fc4"}' --call trading.StockFollow.FollowStock  192.168.100.2:50051`
